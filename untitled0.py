s="BaCoN's cIphEr or THE bacOnIAN CiPHer iS a meThOD oF sTEGaNOGrapHY (a METhoD Of HidIng A sECRet MeSsaGe as OpPOsEd TO a TRUe CiPHeR) dEVIseD BY francis bAcoN. a MessAge Is coNCeALED in THe pRESenTatIoN OF TexT, ratHer thaN iTs coNteNt. tO enCODe A MEsSaGe, eaCh lETter Of THe pLAInText Is rePLAcED By A groUp oF fIvE OF the lETteRs 'a' or 'b'. thIs repLACEMent Is dOnE according to THe alPHabet OF tHe BACOnIAN cIpHeR, sHoWn bElOw. NoTe: A SeCoNd vErSiOn oF BaCoN'S CiPhEr uSeS A UnIqUe cOdE FoR EaCh lEtTeR. iN OtHeR WoRdS, i aNd j eAcH HaS ItS OwN PaTtErN. tHe wRiTeR MuSt mAkE UsE Of tWo dIfFeReNt tYpEfAcEs fOr tHiS CiPhEr. AfTeR PrEpArInG A FaLsE MeSsAgE WiTh tHe sAmE NuMbEr oF LeTtErS As aLl oF ThE As aNd bS In tHe rEaL, sEcReT MeSsAgE, tWo tYpEfAcEs aRe cHoSeN, oNe tO RePrEsEnT As aNd tHe oThEr bS. tHeN EaCh lEtTeR Of tHe fAlSe mEsSaGe mUsT Be pReSeNtEd iN ThE ApPrOpRiAtE TyPeFaCe, AcCoRdInG To wHeThEr iT StAnDs fOr aN A Or a b. To dEcOdE ThE MeSsAgE, tHe rEvErSe mEtHoD Is aPpLiEd. EaCh 'TyPeFaCe 1' LeTtEr iN ThE FaLsE MeSsAgE Is rEpLaCeD WiTh aN A AnD EaCh 'TyPeFaCe 2' LeTtEr iS RePlAcEd wItH A B. tHe bAcOnIaN AlPhAbEt iS ThEn uSeD To rEcOvEr tHe oRiGiNaL MeSsAgE. aNy mEtHoD Of wRiTiNg tHe mEsSaGe tHaT AlLoWs tWo dIsTiNcT RePrEsEnTaTiOnS FoR EaCh cHaRaCtEr cAn bE UsEd fOr tHe bAcOn cIpHeR. bAcOn hImSeLf pRePaReD A BiLiTeRaL AlPhAbEt[2] FoR HaNdWrItTeN CaPiTaL AnD SmAlL LeTtErS WiTh eAcH HaViNg tWo aLtErNaTiVe fOrMs, OnE To bE UsEd aS A AnD ThE OtHeR As b. ThIs wAs pUbLiShEd aS An iLlUsTrAtEd pLaTe iN HiS De aUgMeNtIs sCiEnTiArUm (ThE AdVaNcEmEnT Of lEaRnInG). BeCaUsE AnY MeSsAgE Of tHe rIgHt lEnGtH CaN Be uSeD To cArRy tHe eNcOdInG, tHe sEcReT MeSsAgE Is eFfEcTiVeLy hIdDeN In pLaIn sIgHt. ThE FaLsE MeSsAgE CaN Be oN AnY ToPiC AnD ThUs cAn dIsTrAcT A PeRsOn sEeKiNg tO FiNd tHe rEaL MeSsAgE."
codebook1 = {
    'A':"aaaaa",
    'B':"aaaab",
    'C':"aaaba",
    'D':"aaabb",
    'E':"aabaa",
    'F':"aabab",
    'G':"aabba",
    'H':"aabbb",
    'I':"abaaa",
    'J':"abaab",
    'K':"ababa",
    'L':"ababb",
    'M':"abbaa",
    'N':"abbab",
    'O':"abbba",
    'P':"abbbb",
    'Q':"baaaa",
    'R':"baaab",
    'S':"baaba",
    'T':"baabb",
    'U':"babaa",
    'V':"babab",
    'W':"babba",
    'X':"babbb",
    'Y':"bbaaa",
    'Z':"bbaab",
}
def zhuanhua(s):
    str1=""
    j=0
    for i in s:
        if ord(i)>64 and ord(i)<91:
            str1=str1+"b"
            j=j+1
        elif ord(i)>96 and ord(i)<123:
            str1=str1+'a'
            j=j+1
        if j==5:
            str1+=" "
            j=0
    return str1
def decode(s):
    cipher=""
    ss = s.split(" ")
    for c in ss:
        sign=True
        for k in codebook1.keys():
            if codebook1[k] == c:
                cipher+=k
                sign=False
                break
        if sign:
            #cipher+=c
            pass
    return(cipher)
a=zhuanhua(s)
b=decode(a)
print (b)
mingwen=""
for i in b:
    if i=="X":
        mingwen+=" "
    else:
        mingwen+=i
print (mingwen.lower())