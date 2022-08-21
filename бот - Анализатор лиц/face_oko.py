from deepface import DeepFace


def face_verify(img_1):
    try:
        result_dict = DeepFace.verify(img1_path=[[img_1, 'лица1/Мое.png'], [img_1, 'лица1/Филч.png'],
                                                 [img_1, 'лица1/Серега1.png'], [img_1, 'лица1/Санек.png'],
                                                 [img_1, 'лица1/Фитиль.png'], [img_1, 'лица1/Леха(Саня).png'],
                                                 [img_1, 'лица1/Диман.png']], model_name='Facenet')
        list_answer = []
        list_result = result_dict.get('pair_1')
        if list_result['verified']:
            list_answer.append("Игорь")
        list_result = result_dict.get('pair_2')
        if list_result['verified']:
            list_answer.append("Филч")
        list_result = result_dict.get('pair_3')
        if list_result['verified']:
            list_answer.append("Серега")
        list_result = result_dict.get('pair_4')
        if list_result['verified']:
            list_answer.append("Санек")
        list_result = result_dict.get('pair_5')
        if list_result['verified']:
            list_answer.append("Леха(Фитиль)")
        list_result = result_dict.get('pair_6')
        if list_result['verified']:
            list_answer.append("Леха(Саня)")
        list_result = result_dict.get('pair_7')
        if list_result['verified']:
            list_answer.append("Диман")
        if len(list_answer) != 0:
            return 'принадлежность к суетологам: '+', '.join(list_answer)
        else:
            return 'принадлежность к суетологам: не обнаружена'
    except Exception as _ex:
        return "Сорри, лицо (по крайней мере человеческое) на фото не найдено, попробуйте другое"


def face_analyze(img_1):
    list_race = []
    try:
        result_dict = DeepFace.analyze(img_path=img_1, actions=['age', 'gender', 'race', 'emotion'])
        for a, b in result_dict.get('race').items():
            list_race.append(f'{a} - {round(b, 2)}%')
        return (f'''возраст: {result_dict.get('age')}
пол: {result_dict.get('gender')}
раса: {', '.join(list_race)}
эмоции: {result_dict.get('dominant_emotion')}''')
    except Exception as _ex:
        print("Сорри, лицо (по крайней мере человеческое) на фото не найдено, попробуйте другое")


def main():
    print(face_verify(img_1='лица/илюха.png'))
    face_analyze(img_1='лица/илюха.png')


if __name__ == '__main__':
    main()
