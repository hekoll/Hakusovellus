from cefpython3 import cefpython as cef # kirjasto, jonka avulla piirretään taulukko
import platform # cef vaatii
import base64
import sys
import codecs

from haku import haku


def main():
    sys.excepthook = cef.ExceptHook  # cef alustusta
    cef.Initialize()
    with codecs.open('index.html', encoding="iso-8859-1") as tiedosto:
        html_code = tiedosto.read() # avaa html tiedoston (index.html)

    # print('html', html_code)

    browser = cef.CreateBrowserSync(url=html_to_data_uri(html_code),
                                    window_title="HKA Datatietoja") # ylä otsikko
    set_javascript_bindings(browser) # cef vakio funktio

    cef.MessageLoop()
    cef.Shutdown()

# kutsuu haku funktiota

def hakukutsu(tiedot, tutkimusala, aihe, js_callback):
    result = haku(tiedot, tutkimusala, aihe)
    js_callback.Call(result)


def set_javascript_bindings(browser):
    bindings = cef.JavascriptBindings(
            bindToFrames=False, bindToPopups=False)
    bindings.SetFunction("hakukutsu", hakukutsu) # funktio haku toimii sovelluksessa
    browser.SetJavascriptBindings(bindings)


def html_to_data_uri(html): # luo html tiedoston url:iksi (liittyy cef)
    html = html.encode("utf-8", "replace")
    b64 = base64.b64encode(html).decode("utf-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    return ret

# ajetaan sovellus

if __name__ == '__main__':
    main()
