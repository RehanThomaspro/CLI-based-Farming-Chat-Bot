import random

R_EA1 = "insecticides:for stem borer:fipronil 0.3% /GR,Fungicides:Blast:Isoprothioline 40% /EC for more visit https://timesofagriculture.com/latest-pesticides-list-for-paddy-crop/  https://drdpat.bih.nic.in//Status%20Paper%20-%2002.htm"
R_EA2 = "For weed management :https://agritech.tnau.ac.in/agriculture/agri_weedmgt_wheat.html#:~:text=Spray%20Isoproturon%20800%20g%2Fha,and%2035th%20day%20after%20sowing.   for termites:Thiamethoxam 30% Fs more details on:https://www.dhanuka.com/insecticide/areva-super  "
R_EA3 = "Solution: https://www.agriplexindia.com/index.php/chemical/pesticides/cereals-and-millets/paddy.html?pest_disease=Stem%20Borer&pd_type=0 "
R_EA4 = " solution: https://www.agriplexindia.com/index.php/catalogsearch/result/?q=banana "
R_ADVICE = "Please ask me about a crop"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
