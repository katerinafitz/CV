import pandas as pd

project_list = pd.read_csv("file.csv")
print(project_list)
project_list = project_list.rename(columns={"No.": "Cislo", 
                       "lokalita": "Lokalita", 
                       "Doplňky": "Doplnky", 
                       "Výkon (kW)": "Vykon", 
                       "budget": "Rozpocet",
                       "Celková zákaznická cena bez DPH (CZK)": "Celkova_cena_bez_DPH",
                       "Kontakt-zájem": "Prvni_poptavka",
                       "Odeslána nabídka": "Odeslana_nabidka",
                       " Odeslání žádosti": "Odeslani_zadosti",
                       "uzavření SoD": "Uzavreni_smlouvy_o_dilo",
                       "Vystavena záloha (60%)": "Datum_prvni_zalohy",
                       " 60% z ceny vč. DPH ": "Prvni_zaloha", 
                       "Zaplacena záloha": "Datum_prvni_uhrady",
                       "Zahajení stavby": "Zahajeni_stavby",
                       "Ukončení stavby": "Ukonceni_stavby",
                       "Druhá fakturace (30%)": "Datum_druhe_zalohy",
                       " 30% z ceny vč. DPH ": "Druha_zaloha", 
                       "Zaplacena 2. záloha": "Datum_druhe_uhrady",
                       "Revize provedena": "Datum_revize",
                       "Žádost o PPP": "Zadost_o_PPP",
                       "Předání díla": "Datum_predani", 
                       "Konečná fakturace (10%)": "Datum_treti_zalohy",
                       " 10% z ceny vč. DPH ": "Treti_zaloha",
                       "Doplaceno": "Datum_treti_uhrady", 
                       "Žádost o dotace": "Podani_zadosti_o_dotaci",
                       })
                       
project_list = project_list.drop(columns=["referent",
                                                "ID POHODA",
                                                "ID zakázky",
                                                "název projektu",
                                                "AKU",
                                                "Aktualní stav",
                                                "Telef. kontakt zájemce",
                                                "Osobní návštěva",
                                                "Potvrzení zájmu",
                                                "Technická obhlídka žádost",
                                                "Technická obhlídka doručena",
                                                "Vyjádření od distribuce",
                                                "Materiál",
                                                "Harmonogram výstavby",
                                                "Předání stavby ",
                                                "Revize požadavek",
                                                "Proj. dokumentace požadavek",
                                                "Proj. dokumentace provedena"
                                                ])

project_list["Vykon"] = project_list["Vykon"].str.replace(" kWp", "").str.replace("kWp", "").str.replace(",", ".").str.replace(" kWh", "").str.replace("kWh", "").str.replace(" kwp", "")

project_list["Zdroj"] = project_list["Zdroj"].fillna("")
# project_list[project_list["Zdroj"].str.contains("mail|web|tel")]


project_list.loc[project_list["Zdroj"].str.contains("mail|web|tel"),"Zdroj"] = "Externi"
project_list.loc[~project_list["Zdroj"].str.contains("Externi"),"Zdroj"] = "Interni"

project_list["Rozpocet"] = project_list["Rozpocet"].str.replace(" Kč", "").str.replace(",", "")

project_list["Celkova_cena_bez_DPH"] = project_list["Celkova_cena_bez_DPH"].str.replace(" Kč", "").str.replace(",", "")

project_list["Prvni_zaloha"] = project_list["Prvni_zaloha"].str.replace(" Kč", "").str.replace(",", "")

project_list["Druha_zaloha"] = project_list["Druha_zaloha"].str.replace(" Kč", "").str.replace(",", "")

project_list["Treti_zaloha"] = project_list["Treti_zaloha"].str.replace(" Kč", "").str.replace(",", "")

project_list["Prvni_poptavka"] = project_list["Prvni_poptavka"].str.replace(".","/")
project_list["Odeslana_nabidka"] = project_list["Odeslana_nabidka"].str.replace(".","/")
project_list["Odeslani_zadosti"] = project_list["Odeslani_zadosti"].str.replace(".","/")
project_list["Uzavreni_smlouvy_o_dilo"] = project_list["Uzavreni_smlouvy_o_dilo"].str.replace(".","/")
project_list["Datum_prvni_zalohy"] = project_list["Datum_prvni_zalohy"].str.replace(".","/")
project_list["Datum_prvni_uhrady"] = project_list["Datum_prvni_uhrady"].str.replace(".","/")
project_list["Zahajeni_stavby"] = project_list["Zahajeni_stavby"].str.replace(".","/")
project_list["Ukonceni_stavby"] = project_list["Ukonceni_stavby"].str.replace(".","/")
project_list["Datum_druhe_zalohy"] = project_list["Datum_druhe_zalohy"].str.replace(".","/")
project_list["Datum_druhe_uhrady"] = project_list["Datum_druhe_uhrady"].str.replace(".","/")
project_list["Datum_revize"] = project_list["Datum_revize"].str.replace(".","/")
project_list["Zadost_o_PPP"] = project_list["Zadost_o_PPP"].str.replace(".","/")
project_list["Datum_predani"] = project_list["Datum_predani"].str.replace(".","/")
project_list["Datum_treti_zalohy"] = project_list["Datum_treti_zalohy"].str.replace(".","/")
project_list["Datum_treti_uhrady"] = project_list["Datum_treti_uhrady"].str.replace(".","/")
project_list["Podani_zadosti_o_dotaci"] = project_list["Podani_zadosti_o_dotaci"].str.replace(".","/")

project_list["Status"] = project_list["Status"].replace(to_replace={"U": "Ukonceno", 
                       "N": "Nerealizovano", 
                       "R": "Ukonceno", 
                       "PPP": "Pripojeni",
                       "O": "Odlozeno",
                       "DOT": "Ukonceno",
                       "ZR": "Ukonceno",
                       "D": "Nepotvrzena_realizace", 
                       "CN": "Odeslana_CN", 
                       "Z": "Storno_zakazky",
                       "SoD + D": "Ukonceno",
                       "K": "Odlozeno",
                       "0": "Error"}) 

project_list.to_csv ("project_list.csv",
                  index = None,
                  header = True)
