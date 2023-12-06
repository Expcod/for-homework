#1-masala

def check_letter(func):
    def wrapper(word:str,full_text:list[str]):
        if word in full_text:
            return func(word,full_text)
        return "Matnda bu so'z yo'q!"
    return wrapper

@check_letter
def person(word:str,full_text:list[str])->str:
    return (f"Matnda {word} so'zi bor ")
print(person("salom",["salom", "qish"]))

#2-masala

# def unli_harf_soni(soz):
    
#     unli_harflar = "aeiouAEIOU"
#     soni = sum(1 for harf in soz if harf in unli_harflar)
#     return soni

# soz = "Najot ta'lim"
# natija = unli_harf_soni(soz)
# print(natija)

#3-masala

# def nol_soni(nums:str)->int:
#     return nums.count("0")
# print(nol_soni("2004"))

#4-masala

# def unliga_tekshir(soz1, soz2):

#     unli_harflar = "aeiouAEIOU"
#     mavjud = all(harf in soz2 for harf in soz1 if harf in unli_harflar)
#     return mavjud

# soz1 = "salom"
# soz2 = "Qishda qor yog'armikan"
# natija = unliga_tekshir(soz1, soz2)
# print(natija)


