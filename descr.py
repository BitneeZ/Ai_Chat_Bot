# df = pd.read_csv('labeled.csv')
# print(df)
# file = open('Panama.txt', 'w')
# for index, row in df.iterrows():
#     # print(row, end="")
#     if row['toxic'] == 1.0:
#         print('@Toxic ' + row['comment'], end="")
#         file.write('@Toxic ' + row['comment'])
#     else:
#         print('@Neutral ' + row['comment'], end="")
#         file.write('@Neutral ' + row['comment'])

# df['toxic'] = df['toxic'].replace(1.0, "@Toxic")
# df['toxic'] = df['toxic'].replace(0.0, "@Neutral")
# print(df)
# df['toxic'] = df['toxic'] + "@Toxic"
#
# print(df)

# df.to_csv('toxic4.csv', encoding='utf-8', index=False)

# def load_data():
#     data = {'text':[],'tag':[]}
#     for line in open('Slovar.txt'):
#         if not('#' in line):
#             row = line.split("@")
#             row = [row[1], row[0]]
#             data['tag'] += [row[0]]
#             data['text'] += [row[1]]
#             print(data['tag'])
#             # with open('Panama23.txt', 'a') as file:
#             #     file.write(str(row) + '\n')
#
#
#
# load_data()

# Открываем файл для чтения
# input_file = "slovarmore.txt"  # Замените на имя вашего файла
# output_file = "slovarmore1.txt"  # Имя файла для сохранения результата
#
# # Открываем исходный файл для чтения и создаём новый для записи
# with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
#     for line in infile:
#         # Удаляем всё после символа '@' в строке
#         cleaned_line = line.split('@')[0]
#         # Записываем очищенную строку в новый файл
#         outfile.write(cleaned_line.strip() + "\n")
#
# print(f"Обработка завершена. Очищенный текст сохранён в '{output_file}'.")


#
# # Открываем файл для чтения и создаём новый файл для записи
input_file = "slovarmore3.txt"  # Замените на имя вашего очищенного файла
output_file = "slovarmore4.txt"  # Имя файла для сохранения результата

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        # Убираем перенос строки и добавляем символ @
        updated_line = line.strip() + "@"
        # Записываем обновлённую строку в файл
        outfile.write(updated_line + "\n")

print(f"Обработка завершена. Обновлённый текст сохранён в '{output_file}'.")

#
#
