import json

SAVE_FILE = 'save.jsonl'
QUESTION_FILE = 'china 1.json'
CHARACTER_FILE = 'china_character 1.json'

results = []


def read_people():
    with open(QUESTION_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def save_to_file(results):
    with open(SAVE_FILE, 'a', encoding='utf-8') as jsonl:
        for res in results:
            jsonl.write(json.dumps(res) + '\n')


def display_ans_question(people, name=None):
    skipping = False
    for person in people:
        i = 0
        for question in people[person]:
            print('\n\n========== QUESTION STARTS HERE ==========\n')
            print(f'{person}: {i + 1}/{len(people[person])}\n')
            for line in question:
                print(f"{line}: {question[line]}")

            print('\n\n')
            problem_1 = input("truly most accurate?        :")

            if problem_1 == 'EXIT':
                save_to_file(results)
                print(f"Progress saved to \'save.jsonl\' - progress num: {len(results)}")
                exit(0)

            if problem_1 == 'SKIP':
                i += 1
                continue

            problem_2 = input("incorrect actually correct? :")
            problem_3 = input("incorrect repeated          :")

            temp = {
                'name': person,
                'num': i,
                'q': question['Question'],
                'p1': problem_1,
                'p2': problem_2,
                'p3': problem_3

            }
            results.append(temp)

            i += 1


def get_progress():
    save_data = []

    with open(SAVE_FILE, 'r') as save_file:
        for line in save_file:
            save_data.append(json.loads(line))

    name = save_data[-1]['name']
    return name


def main():
    people = read_people()['china']
    name = get_progress()
    display_ans_question(people, name)
    # print(people)


if __name__ == '__main__':
    main()
