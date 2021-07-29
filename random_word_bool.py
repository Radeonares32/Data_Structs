def kelime_karisikmi(str1, str2):
    for i in str2:
        if i not in str1:
            return False
        return True


kontrol = kelime_karisikmi("sadss", "bugra")
print(kontrol)
