
import os
import csv

election_data_csv_path = os.path.join("Resources, ")
    csvreader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

     vote_count = []
     candidate = []
     percentage = []
     candidate_votes = []
     winner =  []

     total_votes = 0

     for row in candidate_votes:
         name.append(row[0])
         votes.append(row[1])

        candidate_zip = zip(names, votes)
        candidate_list = list(candidate_zip)

        total_votes=len(candidate)

        winner = max(votes)

       
        khan_total = candidate.vote('Khan')
        khan_percent = int(ckhan_total)/ int(total_votes)

        correy_total = candidate.vote('Correy')
        correy_percent = int(correy_total)/ int(total_votes)

        o_tooley_total = candidate.vote('O'Tooley')
        o_tooley_percent = int(otooley_total)/ int(total_votes)

        li_total = candidate.vote('LI')
        li_percent = int(li_total)/ int(total_votes)


        print("Election Results")
ß
        print("----------------------------")

        print("Total Votes":,  ())
        print("Khan:  {khan_percent}:, {khan_total})
        print("Correy: {correy_percent}:, {correy_total})
        print("Li: {li_percent}:, {li_percent})
        print("O'Tooley: {o_tooely_percent}:, {li_percent})

        print("---------------------------")

        print("Winner:   [winner_name}"  )

        print("---------------------------")
