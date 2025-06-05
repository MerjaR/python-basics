# Those who hand in tasks after 3 hours considered to have cheated (task defined on course).
import csv
from datetime import datetime, timedelta
def final_points():
    start_times = {}
    with open("start_times.csv", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            name = row[0]
            time_str = row[1]
            time_obj = datetime.strptime(time_str, "%H:%M").time()
            start_times[name] = time_obj

    best_scores = {}
    
    with open("submissions.csv", encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            name = row[0]
            task = int(row[1])
            points = int(row[2])
            submission_time = datetime.strptime(row[3], "%H:%M").time()

            start_dt = datetime.combine(datetime.today(), start_times[name])
            submit_dt = datetime.combine(datetime.today(), submission_time)

            duration = submit_dt - start_dt
            if duration.total_seconds() > 3 * 60 * 60:
                continue

            if name not in best_scores:
                best_scores[name] = {}
        
            if task not in best_scores[name]:
                best_scores[name][task] = points
            else: 
                best_scores[name][task] = max(best_scores[name][task], points)
        
    final = {}
    for name, tasks in best_scores.items():
        final[name] = sum(tasks.values())

    return final
            
    


    






