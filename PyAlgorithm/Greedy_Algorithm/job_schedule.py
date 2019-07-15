'''
Given a list of jobs with completion time and weight. Find the Optimal schedules that 
minimize the weighted sum of all jobs completion time and weights.
'''

'''
Use score weight/length as score for scheduling each job in decreasing order of the score.
'''


def schedule_jobs(jobs):
    new = sorted(jobs, key=lambda job: job['weight']/job['length'], reverse=True)
    return new


if __name__ == '__main__':
    jobs = []
    job_1 = {'weight': 3, 'length': 2, 'name': 'a'}
    job_2 = {'weight': 3, 'length': 1, 'name': 'b'}
    jobs.append(job_1)
    jobs.append(job_2)
    print "Original: "
    for job in jobs:
        print job['name']
    scheduled = schedule_jobs(jobs)
    print "Schduled: "
    for job in scheduled:
        print job['name']
