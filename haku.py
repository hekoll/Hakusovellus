import pandas

# Tulostus funktio
def js_print(browser, msg):
    browser.ExecuteFunction("js_print", msg)

# Hakufunktio
def haku(tiedot: str, tutkimusala: str, topic: str) -> (str, list):

    # TUTKIMUSTIEDOT
    if tiedot == "Tutkimustiedot":
        # datat (BT = biotiedot, LT = lomaketiedot)
        filenameBT = 'biotiedot_kaikki_pitka.sas7bdat'
        filenameLT = 'lomaketiedot.sas7bdat'

        pBT = pandas.read_sas(filenameBT, encoding='iso-8859-1')
        ppieniBT = pBT.apply(lambda x: x.astype(str).str.lower())
        pLT = pandas.read_sas(filenameLT, encoding='iso-8859-1')
        ppieniLT = pLT.apply(lambda x: x.astype(str).str.lower())

        if tutkimusala == "Biologiset n&auml;ytteet":
            datalistanaBT = pBT.values.tolist()
            return " ", datalistanaBT

        if tutkimusala == "Lomakkeet":
            datalistanaLT = pLT.values.tolist()
            return " ", datalistanaLT


    # BIONÄYTTEET
    if tiedot == "Bionaytteet":
        # data
        filenameB = 'biologisetnaytteet.sas7bdat'
        pB = pandas.read_sas(filenameB, encoding='iso-8859-1')
        ppieniB = pB.apply(lambda x: x.astype(str).str.lower())

        tutkimusala = tutkimusala.lower()

        # korjataan tutkimusaloista pois verkkomerkit
        if tutkimusala == "napaverin&auml;yte":
            tutkimusala = "napaverinäyte"
        if tutkimusala == "nen&auml;tikkun&auml;yte":
            tutkimusala = "nenätikkunäyte"
        if tutkimusala == "poskisolun&auml;yte":
            tutkimusala = "poskisolunäyte"
        if tutkimusala ==  "ulosten&auml;yte":
            tutkimusala = "ulostenäyte"
        if tutkimusala ==  "verin&auml;yte":
            tutkimusala = "verinäytteet"
        if tutkimusala ==  "rintamaiton&auml;yte":
            tutkimusala = "rintamaitonäyte"

        # Haetaan ilman näytettä: tulosta koko taulukko
        if not tutkimusala:
            datalistanaB = pB.values.tolist()
            return "", datalistanaB

        # Haetaan vain näytteellä
        if tutkimusala:
            dataB = ppieniB['Biologinen_nayte'] == tutkimusala
            valittudataB = pB[dataB]

            if valittudataB.empty:
                return "Virhe! N&aumlytett&auml ei olemassa", []

            datalistanaB = valittudataB.values.tolist()
            return "", datalistanaB

    # LOMAKKEET
    if tiedot == "Lomakkeet":
        # data
        filename = 'isodata.sas7bdat'
        p = pandas.read_sas(filename, encoding='iso-8859-1')
        ppieni = p.apply(lambda x: x.astype(str).str.lower())
        p['validoitu'] = p['validoitu'].fillna(0).astype(int)

        tutkimusala = tutkimusala.lower()
        topic = topic.lower()

        # Haku ilman tutkimusalaa
        if not tutkimusala:
            return "Virhe! Valitse tutkimusala", []

        # Haetaan vain tutkimusalalla
        if tutkimusala and not topic:
            data = ppieni['tutkimusala'] == tutkimusala
            valittudata = p[data]

            if valittudata.empty:
                return "Virhe! Tutkimusalaa ei olemassa", []

            datalistana = valittudata.values.tolist()
            return "", datalistana

        # Haetaan tutkimusalalla ja topicilla
        if tutkimusala and topic:
            data1 = ppieni['tutkimusala'] == tutkimusala
            data2 = ppieni['topic'] == topic
            valittudata = p[data1 & data2]

            if valittudata.empty:
                return "Virhe! Tutkimusalaa tai otsikkoa ei olemassa", []

            datalistana = valittudata.values.tolist()
            return "", datalistana
