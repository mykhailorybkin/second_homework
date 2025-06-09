def total_salary(path):
    with open(path) as salary_file:
        try:
            sum_sallary = 0
            
            number_of_workers = 0
            for line in salary_file.readlines():
                if not line.strip():
                    continue
                one_salary = line.split(',')
                sum_sallary = sum_sallary + int(one_salary[1])
                number_of_workers = number_of_workers + 1

            average_sallary = sum_sallary // number_of_workers

            return(average_sallary, sum_sallary)
            

        except:
            return "Error while trying to run the script"
        
average, total = total_salary("salaries.txt")
print(f"Середній розмір зарплат: {average}")
print(f"Загальний розмір зарплати: {total}")