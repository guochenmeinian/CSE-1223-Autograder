import csv
import sys

def main(file_path):

    # Students you need to grade
    students_to_grade = {
        "Li, Kelly",
        "Liu, Andy",
        "Liu, Elizabeth",
        "Liu, Su",
        "Lunay, Simon",
        "Matthews, Jack",
        "Meng, Zhuotong",
        "Messele, Emanuel",
        "Mickle, Brycen",
        "Mohamed, Samira",
        "Munir, Yousuf",
        "Murukuti, Hrushi",
        "Mutai, Cardan",
        "Nutaitis, Jordan",
        "Ojeda, Jd",
        "Osman, Shueyb",
        "Pacheco, Adriana",
        "Panker, Connor",
        "Parasa, Shirish"
    }

    # Store the highest scores of the students
    highest_scores = {}

    # Check and output scores
    with open(file_path, "r", newline='', encoding='utf-8') as file:
        reader = csv.reader(file)

        # Extract header
        header = next(reader)
        
        # Create a mapping of header to its index for easy data extraction
        header_to_idx = {name: index for index, name in enumerate(header)}
        
        for row in reader:
            first_name = row[header_to_idx['first_name']]
            last_name = row[header_to_idx['last_name']]
            student_name = f"{last_name}, {first_name}"
            
            if student_name in students_to_grade:
                max_score = float(row[header_to_idx['max_score']]) if row[header_to_idx['max_score']] else 0
                if student_name in highest_scores:
                    highest_scores[student_name] = max(highest_scores[student_name], max_score)
                else:
                    highest_scores[student_name] = max_score

    for student, score in highest_scores.items():
        print(f"{student}: Max Score = {score}")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to the CSV file as an argument.")
        sys.exit(1)
    csv_path = sys.argv[1]
    main(csv_path)