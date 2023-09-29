import snbtlib
from googletrans import Translator
import os

translator = Translator()

def main():
    #必要な情報を入力してもらう
    print("----FTB-quests-Translater-py----")
    print("Choose your qursts folder (You have to choose the \"\\ftbquests\\quests\" folder):")
    path = input()
    files = os.listdir(path + "\\chapters")
    #すべてのファイルに対してクエストの処理を行う
    for file in files:
        #クエスト一覧を取得
        file_path = path + "\\chapters\\" + file
        #print(file_path)
        #ファイルを開く
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()
        quest_json = snbtlib.loads(data)
        print(quest_json)
        quests = quest_json["quests"]
        translated_quests = [] #翻訳後のクエスト一覧
        #すべてのクエストに対して処理を行う
        for quest in quests:
            if "description" in quest:
                strings = quest["description"]
                translated_strings = [] #各クエストの翻訳後のdescription
                #descriptionが複数に分かれている場合があるので、個別に翻訳する
                for string in strings:
                    print(string)
                    translated = translator.translate(string, dest="ja")
                    translated_string = translated.text
                    print(translated_string)
                    translated_strings.append(translated_string)
                quest["description"] = translated_strings
            translated_quests.append(quest)
        quest_json["quests"] = translated_quests
        print(quest_json)
        print(type(quest_json))
        print("----")
        #ファイルを保存
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(snbtlib.dumps(quest_json))


if __name__ == "__main__":
    main()