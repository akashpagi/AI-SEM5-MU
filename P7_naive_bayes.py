rwp_examples = dict(
    x1=dict(Alt='Y', Bar='N', Fri='N',Hun='Y',Pat='S',Price='$$$',Rain='N',Res='Y',Type='F',Est='0-10',ans='Y'),
    x2=dict(Alt='Y', Bar='N', Fri='N',Hun='Y',Pat='F',Price='$',Rain='N',Res='N',Type='T',Est='30-60',ans='N'),
    x3=dict(Alt='N', Bar='Y', Fri='N',Hun='N',Pat='S',Price='$',Rain='N',Res='N',Type='B',Est='0-10',ans='Y'),
    x4=dict(Alt='Y', Bar='N', Fri='Y',Hun='Y',Pat='F',Price='$',Rain='Y',Res='N',Type='T',Est='10-30',ans='Y'),
    x5=dict(Alt='Y', Bar='N', Fri='Y',Hun='N',Pat='F',Price='$$$',Rain='N',Res='Y',Type='F',Est='>60',ans='N'),
    
    )

total_exp = 5
def tot(attribute, value):
    count = 0
    for key, val in rwp_examples.items():
        for key1, val1 in val.items():
            if key1 == attribute:
                if val1 == value:
                    count += 1
    return count
def getProbab(attribute, attribval, value):
    count = 0
    for key, val in rwp_examples.items():
        val1 = rwp_examples[key][attribute]
        val2 = rwp_examples[key]['ans']
        if val1 == attribval and val2 == value:
            count += 1
    probab = count / tot('ans', value)
    return probab
def main():
    PAltYes = tot('Alt', 'Y') / total_exp
    PAltNo = tot('Alt', 'N') / total_exp    
    PPatSome = tot('Pat', 'S') / total_exp    
    PEstFew = tot('Est', '0-10') / total_exp
    PEstMore = tot('Est', '10-30') / total_exp
    PEstStillMore = tot('Est', '30-60') / total_exp
    PEstTooMuch = tot('Est', '>60') / total_exp
    PAnsYes = tot('ans', 'Y') / total_exp
    PAnsNo = tot('ans', 'N') / total_exp    
    print('Probability for will wait if there is an Alternate Restaurant Nearby: ')
    print('Yes: Will Wait ', (getProbab('Alt', 'Y', 'Y') * PAnsYes/PAltYes) * 100, '%')
    print('No: Will Wait ', (getProbab('Alt', 'Y', 'N') * PAnsNo/PAltYes ) * 100, '%')
    print('Probability for will wait if there No is an Alternate Restaurant Nearby: ')
    print('Yes: Will Wait ', (getProbab('Alt', 'N', 'Y') * PAnsYes/PAltNo) * 100, '%')
    print('No: Will Wait ', (getProbab('Alt', 'N', 'N') * PAnsNo/PAltNo) * 100, '%')
    print('Probability for will wait if Estimated Wait time is 0-10 minutes: ')
    print('Yes: Will Wait ', (getProbab('Est', '0-10', 'Y') * PAnsYes/PEstFew) * 100, '%')
    print('No: Will Wait ', (getProbab('Est', '0-10', 'N') * PAnsNo/PEstFew) * 100, '%')
    print('Probability for will wait if Estimated Wait time is 10-30 minutes ')
    print('Yes: Will Wait ', (getProbab('Est', '10-30', 'Y') * PAnsYes/PEstMore) * 100, '%')
    print('No: Will Wait ', (getProbab('Est', '10-30', 'N') * PAnsNo/PEstMore) * 100, '%')
    print("Probability for Will Wait if the Estimated Wait Time is 30-60 mins: ")
    print("Yes: Will Wait: ",(getProbab('Est','30-60','Y')*PAnsYes/PEstStillMore)*100,"%")
    print("No: Will Wait: ",(getProbab('Est','30-60','N')*PAnsNo/PEstStillMore)*100,"%")
    print("Probability for Will Wait if the Estimated Wait Time is >60 mins: ")
    print("Yes: Will Wait: ",(getProbab('Est','>60','Y')*PAnsYes/PEstTooMuch)*100,"%")
    print("No: Will Wait: ",(getProbab('Est','>60','N')*PAnsNo/PEstTooMuch)*100,"%")
    print('Probability for will wait if there are Some Patrons ')
    print('Yes: Will Wait ', (getProbab('Pat', 'S', 'Y') * PAnsYes/PPatSome) * 100, '%')
    print('No: Will Wait ', (getProbab('Pat', 'S', 'N') * PAnsNo/PPatSome) * 100, '%')
        
main()

