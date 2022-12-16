def save_to_csv(new_contacts):
    with open('phonebook.csv', 'a') as bd:
        for i in range(len(new_contacts)):
            if i != len(new_contacts) - 1:
                bd.write(f'{new_contacts[i]};')
            else:
                bd.write(f'{new_contacts[i]}')
        bd.write('\n')