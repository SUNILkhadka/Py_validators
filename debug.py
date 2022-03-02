
text = '''
    A risk management plan is a key component of a success project. 
    In the early days of program management aspects such as cost, and schedule were often favored for making decisions because teams understood schedule and cost (Kerzner, 2017). 
    In recent years there has been an increase focus on risk management due to the rapidly changing business environment and the dangers that unmanaged risks can pose to projects.
    Companies that make risk management an integral part of their program management theology are taking steps to prevent setbacks, schedule slips, and budget over runs. 
    This is best accomplished by developing a robust systematic process for identifying, analyzing, planning, monitoring, and closure of project risks. 
    This systematic approach puts business in a position to be proactive about uncertainty instead of reactive which ultimately sets the team up for success.
    Risk management may cost projects budget and time up front but can save much more in the long run.
    Risk is is defined as the uncertainty that an event or condition may occur and will have an impact on one or more of the project objectives; scope, schedule, cost, or quality (Soliman, 2018).
    Risk management is becoming more important as companies launch larger, more complex projects that have aggressive schedules, budgets, and commitments to stay competitive in the dynamic business environment. 
    Risk is inherent to any project which can be influence by internal and external sources that may not be within the teams control. When teams attempt to manage risk, it is critical to, when possible, manage the source of the risk instead of the risk itself. 
    A detailed understanding of root cause is crucial before teams move forward with resolution. 
    Addressing a risk source gives the team the power to solve the root of the risk which may address more than one risk at a time (Tiendung et al, 2009). 
    Without fully addressing the root cause there is a risk that the solution will not fully address the risk or that the solution may create risk in the process. In physics there is a reaction for every action. 
    This is no different in project management which is why it is important to have a proper action to ensure the reaction is positive. 
    Organizations who understand this and take the time to develop and utilize robust risk management processes have a much higher chance for successfully completing a project on time and on budget (Baharuddin & Yusof, 2018). 
    Without a process for risk management companies are putting themselves at risk for failure.
'''


def search(text,keyword):
    count = 0
    result = []
    for x in text:
        if x.find(keyword) > 0:
            result.append(x+'.\n')
            count+=1
    print(result)
    if count == 0:
        print('Not Found')
    else:
        print("Found in '",count,"' sentence")
        
txt = ['A risk management.', 'In recent risk years there has been an Accident .\n', 'This is best accomplished.\n']
search(txt,'risk')

