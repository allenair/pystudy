import easyocr
reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
result = reader.readtext('d:/chinese.png', detail = 0)

print(result)