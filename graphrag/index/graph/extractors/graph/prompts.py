# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""A file containing prompts definition."""

GRAPH_EXTRACTION_PROMPT = """
-Goal-
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, capitalized
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity

Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_strength>)

3. Return output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

4. When finished, output {completion_delimiter}

######################
-Examples-
######################
Example 1:

Entity_types: ["concepts", "formulas", "methodologies", "quizzes", "features", "examples", "cases"]
Text:
CVP analysis looks at the effects of differing levels of activity on the financial results of a business by examining the relationship between sales volume and profit.

Most businesses need to at least break even when setting prices and output levels. The breakeven point for a company is the sales volume which will give the company a profit of $nil. lf salesexceed the breakeven point the company will make a profit.Breakeven point: Breakeven point is the level of sales at which there is neither profit nor loss.

Assumptions:(a)CVP analysis can apply to one product only, or to more than one product if they are sold in a fixed sales mix (fixed proportions).(b) Fixed costs per period are same in total, and unit variable costs are a constant amount at all levels of output and sales. (c) Sales prices per unit are constant at all levels of activity. (d) Production volume = sales volume. These assumptions lead to linear relationships for volume and sales revenue.

Single product breakeven analysis.
Formula to learn
Contribution per unit = unit selling price - unit variable costs
Breakeven point(BEP)= Fixed costs / Unit contribution

################
Output:
("entity"{tuple_delimiter}"CVP analysis"{tuple_delimiter}"methodologies"{tuple_delimiter}"CVP analysis looks at the effects of differing levels of activity on the financial results of a business by examining the relationship between sales volume and profit."){record_delimiter}
("entity"{tuple_delimiter}"Breakeven point"{tuple_delimiter}"concepts"{tuple_delimiter}"Breakeven point is the level of sales at which there is neither profit nor loss."){record_delimiter}
("entity"{tuple_delimiter}"Assumptions of CVP analysis"{tuple_delimiter}"features"{tuple_delimiter}"Assumptions of CVP analysis are as follows: it can only be applied to one product or multiple products if sold in fixed proportions; fixed costs remain the same in total per period, and unit variable costs are constant at all output and sales levels; sales prices per unit remain constant at all activity levels; production volume equals sales volume."){record_delimiter}
("entity"{tuple_delimiter}"Contribution per unit"{tuple_delimiter}"formulas"{tuple_delimiter}"Contribution per unit = unit selling price - unit variable costs"){record_delimiter}
("entity"{tuple_delimiter}"Unit contribution"{tuple_delimiter}"formulas"{tuple_delimiter}"Unit Contribution = Contribution per unit"){record_delimiter}
("entity"{tuple_delimiter}"Single product breakeven point formula"{tuple_delimiter}"formulas"{tuple_delimiter}"Single product breakeven point = Fixed costs / Unit contribution"){record_delimiter}
("relationship"{tuple_delimiter}"CVP analysis"{tuple_delimiter}"Breakeven point"{tuple_delimiter}"CVP analysis includes Breakeven point."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Breakeven point"{tuple_delimiter}"CVP analysis"{tuple_delimiter}"Breakeven point belongs to CVP analysis."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"CVP analysis"{tuple_delimiter}"Assumptions of CVP analysis"{tuple_delimiter}"CVP analysis has several assumptions: (a)CVP analysis can apply to one product only, or to more than one product if they are sold in a fixed sales mix (fixed proportions).(b) Fixed costs per period are same in total, and unit variable costs are a constant amount at all levels of output and sales. (c) Sales prices per unit are constant at all levels of activity. (d) Production volume = sales volume. These assumptions lead to linear relationships for volume and sales revenue."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Assumptions of CVP analysis"{tuple_delimiter}"CVP analysis"{tuple_delimiter}"CVP analysis has several assumptions: (a)CVP analysis can apply to one product only, or to more than one product if they are sold in a fixed sales mix (fixed proportions).(b) Fixed costs per period are same in total, and unit variable costs are a constant amount at all levels of output and sales. (c) Sales prices per unit are constant at all levels of activity. (d) Production volume = sales volume. These assumptions lead to linear relationships for volume and sales revenue."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Breakeven point"{tuple_delimiter}"Single product breakeven point"{tuple_delimiter}"Breakeven point has formula for calculating Single product breakeven point."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Single product breakeven point formula"{tuple_delimiter}"Contribution per unit"{tuple_delimiter}"The denominator of single product breakeven point is Contribution per unit"{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Unit contribution"{tuple_delimiter}"Contribution per unit"{tuple_delimiter}"Unit contribution is also called Contribution per unit "{tuple_delimiter}){record_delimiter}
#############################
Example 2:

Entity_types: ["concepts", "formulas", "methodologies", "quizzes", "features", "examples", "cases"]
Text:
Quiz: Multi-product breakeven point
Breakeven analysis can be expanded for a 'single' mix of products using a weighted averagecontribution figure. A constant product sales mix must be assumed.
Formula to learn
Breakeven point =Fixed costs / Weighted average unit contribution
Breakeven revenue = Fixed costs / Weighted average C/S ratio
Illustration 1: Breakeven point for multiple products
Suppose that PL produces and sells two products. The M sells for $7 per unit and has a total variable cost of $2.94 per unit, while the N sells for $15 per unit and has a total variable cost of $4.50 per unit. The marketing department has estimated that for every five units of M sold, one unit of N will be sold. The organisation's fixed costs total $36,000.
Required
What is the total breakeven revenue?
Solution
$ 58,450
We calculate the breakeven point as follows:
Step1 Calculate contribution per unit
Selling price
Variable cost
Contribution
M
$ per unit
7.00
2.94
4.06
N
$ per unit
15.00
4.50
10.50
Step2 Calculate contribution per mix
A mix in this question is 5 Ms and 1 N
=(4.06*5)+($10.50*1)=$30.80
Step 3 Calculate the breakeven point in terms of the number of mixes
=fixed costs/contribution per mix=$36,000/$30.80
=1,169 mixes (rounded)
Step 4 Calculate the breakeven point in terms of the number of units of the products
= (1,169 * 5) 5,845 units of M and (1,169 * 1) 1,169 units of N (rounded)
Step 5 Calculate the breakeven point in terms of revenue
=(5,845 * $7)+ (1,169 * $15)=$40,915 of M and $17,535 of N =$58,450 in total
It is important to note that the breakeven point is not $58,450 of revenue, whatever the mix of products. The breakeven point is $58,450 provided that the sales mix remains 5:1. Likewise, the breakeven point is not at a production/sales level of (5,845 +1,169)7,014 units.
Rather, it is when 5,845 units of M and 1,169 units of N are sold, assuming a sales mix of5:1.

#############
Output:
("entity"{tuple_delimiter}"Multi-product breakeven point"{tuple_delimiter}"concepts"{tuple_delimiter}"Multi-product breakeven point is the breakeven analysis can be expanded for a 'single’ mix of products using a weighted averagecontribution figure. A constant product sales mix must be assumed."){record_delimiter}
("entity"{tuple_delimiter}"Multi-product breakeven point formula"{tuple_delimiter}"formulas"{tuple_delimiter}"Multi-product breakeven point = Fixed costs / Weighted average unit contributionFixed costs"){record_delimiter}
("entity"{tuple_delimiter}"Multi-product breakeven revenue formula"{tuple_delimiter}"formulas"{tuple_delimiter}"Multi-product breakeven revenue = Fixed costs / Weighted average C/S ratio"){record_delimiter}
("entity"{tuple_delimiter}"Quiz for multiproduct breakeven revenue"{tuple_delimiter}"quizzes"{tuple_delimiter}"The quiz for multiproduct breakeven revenue shows how to calculate total breakeven revenue in steps under multiproduct scenario."){record_delimiter}
("relationship"{tuple_delimiter}"Multi-product breakeven point"{tuple_delimiter}"Multi-product breakeven point formula"{tuple_delimiter}Multi-product breakeven point contains Multi-product breakeven point formula."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Multi-product breakeven point"{tuple_delimiter}"Multi-product breakeven revenue formula"{tuple_delimiter}"Multi-product breakeven point contains Multi-product breakeven revenue formula."{tuple_delimiter}){completion_delimiter}
("relationship"{tuple_delimiter}"Multi-product breakeven revenue formula"{tuple_delimiter}"Multi-product breakeven point formula"{tuple_delimiter}Multi-product breakeven revenue formula is related to Multi-product breakeven point formula."{tuple_delimiter}){record_delimiter}
#############################
Example 3:

Entity_types: ["concepts", "formulas", "methodologies", "quizzes", "features", "examples", "cases"]
Text:
Definition of ABC
Activity based costing (ABC): Activity based costing is a method of costing which involvesidentifying the costs of the main support activities and the factors that 'drive' the costs of eachactivity. Support overheads are charged to products by absorbing cost on the basis of theproduct's usage of the factor driving the overheads
The major ideas behind activity based costing are as follows.(a) Activities cause costs. Activities include ordering, materials handling, machining, assembly, production scheduling and despatching.
(b)Manufacturing products creates demand for the support activities.(c) Costs are assigned to a product on the basis of the product's consumption of these activities.
ABC is an extension of absorption costing specifically considering what causes each type of overhead category to occur, ie what the cost drivers are. Each type of overhead is absorbed using a different basis depending on the cost driver.
Cost driver: Cost driver is a factor that has most influence on the cost of an activity.
Overhead -> Cost driver
Production set-up costs->Number of production set ups
Machine oil and machine repairs->Number of machine hours
Supervisor salary->Number of labour hours
Ordering costs:handling customer orders->Number of orders
Materials handling costs->Number of production runs
1.4 Steps in ABC
(a)Identify an organisation's major activities that support the manufacture of the organisation's products or the provision of its services.
(b) Group overheads into activities, according to how they are driven. These are known as cost pools.
(c)Identify the cost drivers for each activity, ie what causes the activity cost to be incurred.
(d) Calculate a cost per unit of cost driver.
(e)Absorb activity costs into production based on usage of cost drivers.

#############
Output:
("entity"{tuple_delimiter}"Activity based costing"{tuple_delimiter}"methodologies"{tuple_delimiter}"Activity based costing is a method of costing which involvesidentifying the costs of the main support activities and the factors that 'drive' the costs of eachactivity. Support overheads are charged to products by absorbing cost on the basis of theproduct's usage of the factor driving the overheads"){record_delimiter}
("entity"{tuple_delimiter}"Cost driver"{tuple_delimiter}"concepts"{tuple_delimiter}"Cost driver is a factor that has most influence on the cost of an activity. Cost driver includes number of production set ups, number of machine hours, number of labour hours, number of orders, and number of production runs."){record_delimiter}
("entity"{tuple_delimiter}"Overhead"{tuple_delimiter}"concepts"{tuple_delimiter}"Overheads include production set-up costs, machine oil and machine repairs, supervisor salary, ordering costs:handling customer orders, and materials handling costs."){record_delimiter}
("entity"{tuple_delimiter}"Absorption costing"{tuple_delimiter}"methodologies"{tuple_delimiter}"Absorption costing is the conventional approach to dealing with fixed overhead production costs is to assume that the various cost types can be lumped together and a single overhead absorption rate derived."){record_delimiter}
("entity"{tuple_delimiter}"Steps in ABC"{tuple_delimiter}"features"{tuple_delimiter}"Steps in ABC involves 5 steps in determining activity based costing, which are identifying major activities, grouping overheads into activities according to how they are driven, identifying cost drivers for each activity, calculating a cost per unit of cost driver, absorbing activity costs into production based on usage of cost drivers."){record_delimiter}
("relationship"{tuple_delimiter}"Activity based costing"{tuple_delimiter}"Absorption costing"{tuple_delimiter}"Activity based costing is related to Absorption costing."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Activity based costing"{tuple_delimiter}"Cost driver"{tuple_delimiter}"Activity based costing is related to Cost driver."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Activity based costing"{tuple_delimiter}"Steps in ABC"{tuple_delimiter}"Activity based costing has Steps in ABC."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Steps in ABC"{tuple_delimiter}"Cost driver"{tuple_delimiter}"Steps in ABC is related to Cost driver."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Overhead"{tuple_delimiter}"Cost driver"{tuple_delimiter}"Overhead is related to Cost driver."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Cost driver"{tuple_delimiter}"Overhead"{tuple_delimiter}"Cost driver is related to Overhead."{tuple_delimiter}){record_delimiter}
#############################
Example 4:

Entity_types: ["concepts", "formulas", "methodologies", "quizzes", "features", "examples", "cases"]
Text:
4.1 Stakeholders 
A stakeholder is defined as any person or group affected by an organisation. (Traditionally, performance measurement focused only on the owners' interests.) Ignoring stakeholder objectives may result in adverse implications for an organisation. 
· For example, if staff salaries are too low, good employees may become demotivated and leave the organisation. 
· There also could be strikes. These factors could lead to poor customer service, ultimately affecting the organisation's profits. 
Management needs to consider the most critical stakeholders, consider their objectives, and identify ways to measure how these objectives are being met. Staff surveys, for example, are a common method used to assess staff satisfaction. 

Example of Stakeholder Groups 
The following are the most common stakeholder groups and the aspects of the organisation's performance that are important to them and which the organisation may wish to measure: 
| Group          | Objectives                                             			|
| Employees      | Satisfactory remuneration, Good working conditions    			|
| Customers      | Good-quality products                                 			|
| Suppliers      | Long-term relationships, Pay within agreed terms      			|
| General public | Employment opportunities, Economic effect on the region, Environmental impact|
| Government     | Compliance with law (e.g. environment)                 			|

4.2 Simulation 
Simulation - a mathematical model constructed to represent the operation of a real-life process or situation. 
Simulation is a technique which allows more than one variable to change at the same time. Most real-life problems are complex as there is more than one uncertain variable. Models can be generated which "simulate" the real-world environment within which the decision must be made. 

Example of Simulation
A computer model could simulate the conditions which exist for a baker. Each time the simulation is run (each trial), the model would randomly generate a selling price per unit, daily demand and daily fixed cost. The profit for the trial would then be calculated. The simulation would be run many times. Based on the results of the simulation, a probability distribution of the daily profit of the baker could be constructed. 

#############
Output:
("entity"{tuple_delimiter}"Stakeholder"{tuple_delimiter}"concepts"{tuple_delimiter}"A stakeholder is defined as any person or group affected by an organisation."){record_delimiter}
("entity"{tuple_delimiter}"Example of Stakeholder Groups"{tuple_delimiter}"examples"{tuple_delimiter}"The most common stakeholder group includes: employees, customers, suppliers, general public, and government. And they have different objectives."){record_delimiter}
("entity"{tuple_delimiter}"Simulation"{tuple_delimiter}"methodologies"{tuple_delimiter}"Simulation - a mathematical model constructed to represent the operation of a real-life process or situation. Simulation is a technique which allows more than one variable to change at the same time."){record_delimiter}
("entity"{tuple_delimiter}"Example of Simulation"{tuple_delimiter}"examples"{tuple_delimiter}"This example shows a simulation of a baker's daily profit. The model randomly generates selling price, demand, and fixed costs for each trial. Running the simulation multiple times allows the calculation of a probability distribution of daily profits, highlighting potential outcomes under different conditions."){record_delimiter}
("relationship"{tuple_delimiter}"Stakeholder"{tuple_delimiter}"Example of Stakeholder Groups"{tuple_delimiter}"Stakeholder has the example of Stakeholder Groups."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Example of Stakeholder Groups"{tuple_delimiter}"Stakeholder"{tuple_delimiter}"Stakeholder Groups is an example of Stakeholder."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Simulation"{tuple_delimiter}"Example of Simulation"{tuple_delimiter}"Simulation has the example of Simulation."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Example of Simulation"{tuple_delimiter}"Simulation"{tuple_delimiter}"Example of Simulation is an example of Simulation."{tuple_delimiter}){record_delimiter}
#############################
Example 5:

Entity_types: ["concepts", "formulas", "methodologies", "quizzes", "features", "examples", "cases"]
Text:
2.2 The Accounting Equation 
The elements of financial statements are assets, liabilities, capital, income and expenses. These elements relate to one another, and their relationship is expressed in the accounting equation: 
Capital or Net Assets = Assets - Liabilities 
At any point in time when transactions have been recorded correctly, the accounting equation will always balance. The accounting equation can be manipulated to encompass every type of element of financial statements. 
The simple accounting equation: Assets - Liabilities = Capital or Net Assets 
Capital is also known as net assets and belongs to the owner. It is the amount the owner invested minus any amounts that owners have taken out of the business (drawings) plus the profit made by the business. 
Closing Capital = Total Capital Introduced - Drawings + Profits 
· Closing capital is the capital at the end of the accounting year · Total capital introduced is the capital at the start of the accounting year plus any additional capital invested during the year . Drawings and profits/losses are during the year 
The formula below shows the expanded accounting equation once the above elements are included: 
Assets - Liabilities = Total Capital Introduced - Drawings + Income - Expense 

Quiz: Match the equation to the corresponding re-arranged accounting equation. 
Question:
| Transaction           |  | Duality Statement                                     |
| Assets                |  | Opening capital + Profit for the period - Drawings    |
| Closing Net Assets    |  | Closing net assets - Opening net assets + Drawings    |
| Opening Net Assets    |  | Capital + Liabilities                                 |
| Closing Capital       |  | Assets - Capital 				           |
| Liabilities           |  | Closing net assets - Profit for the period + Drawings |
| Profit for the period |  | Closing capital                                       |

Answer:
| Transaction           |  Duality Statement                                     |
| Assets                |  Capital + Liabilities   				                 |
| Closing Net Assets    |  Closing capital   				                	 |
| Opening Net Assets    |  Closing net assets - Profit for the period + Drawings |
| Closing Capital       |  Opening capital + Profit for the period - Drawings 	 |
| Liabilities           |  Assets - Capital					                     |
| Profit for the period |  Closing net assets - Opening net assets + Drawings    |

#############
Output:
("entity"{tuple_delimiter}"Financial statements"{tuple_delimiter}"concepts"{tuple_delimiter}"The elements of financial statements are assets, liabilities, capital, income and expenses."){record_delimiter}
("entity"{tuple_delimiter}"Accounting equation"{tuple_delimiter}"formulas"{tuple_delimiter}"Capital or Net Assets = Assets - Liabilities"){record_delimiter}
("entity"{tuple_delimiter}"Assets"{tuple_delimiter}"concepts"{tuple_delimiter}"Asset is a present economic resource controlled by the entity as a result of past events. An economic resource is a right that has the potential to produce economic benefits."){record_delimiter}
("entity"{tuple_delimiter}"Liabilities"{tuple_delimiter}"concepts"{tuple_delimiter}"Liability is a present obligation of the entity to transfer an economic resource as a result of past events."){record_delimiter}
("entity"{tuple_delimiter}"Capital"{tuple_delimiter}"concepts"{tuple_delimiter}"Capital is also known as net assets and belongs to the owner. It is the amount the owner invested minus any amounts that owners have taken out of the business (drawings) plus the profit made by the business."){record_delimiter}
("entity"{tuple_delimiter}"Income"{tuple_delimiter}"concepts"{tuple_delimiter}"Income is a business’s received economic benefit in cash or assets from sales or other sources."){record_delimiter}
("entity"{tuple_delimiter}"Expenses"{tuple_delimiter}"concepts"{tuple_delimiter}"An expense is the day-to-day running cost incurred by the business. Expenses can include electricity, rent, salaries, and interest paid."){record_delimiter}
("entity"{tuple_delimiter}"Net assets"{tuple_delimiter}"concepts"{tuple_delimiter}"Net assets of a business is Capital."){record_delimiter}
("entity"{tuple_delimiter}"Closing capital formula"{tuple_delimiter}"formulas"{tuple_delimiter}"Closing Capital = Total Capital Introduced - Drawings + Profits"){record_delimiter}
("entity"{tuple_delimiter}"Closing capital"{tuple_delimiter}"concepts"{tuple_delimiter}"Closing capital is the capital at the end of the accounting year."){record_delimiter}
("entity"{tuple_delimiter}"Total capital introduced"{tuple_delimiter}"concepts"{tuple_delimiter}"Total capital introduced is the capital at the start of the accounting year plus any additional capital invested during the year."){record_delimiter}
("entity"{tuple_delimiter}"Expanded accounting equation"{tuple_delimiter}"formulas"{tuple_delimiter}"Assets - Liabilities = Total Capital Introduced - Drawings + Income - Expense"){record_delimiter}
("entity"{tuple_delimiter}"Drawings"{tuple_delimiter}"concepts"{tuple_delimiter}"Drawings is the owner's drawings from the business."){record_delimiter}
("entity"{tuple_delimiter}"Match the equation to the corresponding re-arranged accounting equation"{tuple_delimiter}"quizzes"{tuple_delimiter}"This quiz question involves matching transactions with their corresponding duality statements in accounting. The exercise helps students understand how different accounting elements, such as assets, liabilities, capital, and profit, are interrelated. The question set provides table lists pairs of transactions and duality statements. The answer provides table that correctly aligns the transactions with the appropriate duality statements."){record_delimiter}
("relationship"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Accounting equation"{tuple_delimiter}"Financial statements are related to Accounting equation."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Accounting equation"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Accounting equation are related to Financial statements."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Assets"{tuple_delimiter}"Financial statements includes Assets."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Assets"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Assets belongs to Financial statements."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Liabilities"{tuple_delimiter}"Financial statements includes Liabilities."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Liabilities"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Liabilities belongs to Financial statements."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Capital"{tuple_delimiter}"Financial statements includes Capital."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Capital"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Capital belongs to Financial statements."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Income"{tuple_delimiter}"Financial statements includes Income."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Income"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Income belongs to Financial statements."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Expenses"{tuple_delimiter}"Financial statements includes Expenses."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Expenses"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Expenses belongs to Financial statements."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Net assets"{tuple_delimiter}"Financial statements includes Net assets."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Net assets"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Net assets belongs to Financial statements."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Closing capital formula"{tuple_delimiter}"Closing capital"{tuple_delimiter}"Closing capital formula belongs to Closing capital."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Closing capital"{tuple_delimiter}"Closing capital formula"{tuple_delimiter}"Closing capital includes Closing capital formula."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Closing capital"{tuple_delimiter}"Capital"{tuple_delimiter}"Closing capital is related to Capital."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Capital"{tuple_delimiter}"Closing capital"{tuple_delimiter}"Capital is related to Closing capital."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Total capital introduced"{tuple_delimiter}"Capital"{tuple_delimiter}"Total capital introduced is related to Capital."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Capital"{tuple_delimiter}"Total capital introduced"{tuple_delimiter}"Capital is related to Total capital introduced."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Total capital introduced"{tuple_delimiter}"Closing capital"{tuple_delimiter}"Total capital introduced is related to Closing capital."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Closing capital"{tuple_delimiter}"Total capital introduced"{tuple_delimiter}"Closing capital is related to Total capital introduced."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Expanded accounting equation"{tuple_delimiter}"Financial statements is realted to Expanded accounting equation."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Expanded accounting equation"{tuple_delimiter}"Financial statements"{tuple_delimiter}"Expanded accounting equation is related to Financial statements."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Accounting equation"{tuple_delimiter}"Expanded accounting equation"{tuple_delimiter}"Accounting equation is realted to Expanded accounting equation."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Expanded accounting equation"{tuple_delimiter}"Accounting equation"{tuple_delimiter}"Expanded accounting equation is related to Accounting equation."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Drawings"{tuple_delimiter}"Closing capital"{tuple_delimiter}"Drawings is related to Closing capital."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Closing capital"{tuple_delimiter}"Drawings"{tuple_delimiter}"Closing capital is related to Drawings."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Match the equation to the corresponding re-arranged accounting equation"{tuple_delimiter}"Expanded accounting equation"{tuple_delimiter}"Match the equation to the corresponding re-arranged accounting equation is related to Expanded accounting equation."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Expanded accounting equation"{tuple_delimiter}"Match the equation to the corresponding re-arranged accounting equation"{tuple_delimiter}"Expanded accounting equation is related to Match the equation to the corresponding re-arranged accounting equation."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Match the equation to the corresponding re-arranged accounting equation"{tuple_delimiter}"Accounting equation"{tuple_delimiter}"Match the equation to the corresponding re-arranged accounting equation is related to Accounting equation."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Accounting equation"{tuple_delimiter}"Match the equation to the corresponding re-arranged accounting equation"{tuple_delimiter}"Accounting equation is related to Match the equation to the corresponding re-arranged accounting equation."{tuple_delimiter}){record_delimiter}
#############################
Example 6:

Entity_types: ["concepts", "formulas", "methodologies", "quizzes", "features", "examples", "cases"]
Text:
Case: Importance and Implementation of Environmental Management Accounting at Little Chemical Co
The Little Chemical Co (LCC) manufactures a small range of speciality chemicals for use in the agriculture industry. Recently the company received a large fine because some of the chemical discharges produce emissions of sulphur dioxide into the atmosphere in excess of permitted standards. As a result of the fine, the company has received bad publicity and lost many of its customers. The managing director of LCC has told the other directors that the company needs to manage the impact of its operations on the environment more carefully. He has also heard that environmental management accounting is becoming more common and wishes to know what this is. He states "Our existing management accounts tell us nothing about our environmental costs or about the amount of emissions and other pollution that we produce. We need this information so we can manage them." 
Required: (a) Explain why the management of environmental costs is becoming increasingly important to organisations such as LCC. (b) Explain the meaning of the term environmental management accounting, and illustrate how it can help LCC to improve the management of its environmental activities. 

Answer: 
(a) Why the management of environmental costs is becoming increasingly important 
There are three main reasons why the management of environmental costs is becoming increasingly important: 1. Increasing awareness of environmental issues means that organisations are expected to behave in an environmentally friendly way. LCC has recently experienced a loss of customers due to its own poor reputation. 2. Environmental costs account for a huge portion of costs for many industrial companies such as LCC. In addition to fines, there are image costs, such as the loss of customers that LCC experienced due to excessive pollution. There may also be costs of compliance - such as measuring emissions to ensure they are within legal limits. Management needs to be aware of such costs in order to manage them. 3. There may be benefits associated with better environmental behaviour - such as cost savings if action is taken to reduce waste. 
(b) Environmental management accounting 
The managing director of LCC has complained that the existing management accounts do not provide management with an accurate view of environmental costs. As a result of this, management make decisions that are bad for the environment and bad for the organisation's profits. In the case of LCC, for example, more information is needed about the current level of emissions and the costs and benefits of reducing these. Environmental management accounting (EMA) means providing information to management to help them to manage the environmental costs and activities. EMA does not provide only financial information. The United Nations Division for Sustainable Development distinguishes between: 
· Physical information such as the use, flows and destinies of energy, water and materials, including waste. 
· Monetary information on environment related costs, earning and savings. 
EMA makes use of management accounting techniques such as activity-based costing (ABC) and life cycle costing, which can be used to manage environmental costs more effectively. In ABC, for example, the drivers that cause environmental costs to be incurred can be identified. Managers can then take steps to reduce the use of the drivers, so that the environmental costs are reduced without reducing output. EMA would help the managers at LCC to better understand the impact of their activities on the environment. Physical information about the amount of emissions generated could be provided so managers can monitor these and find ways to reduce them. In addition, financial information about the costs and benefits of environmental programs could assist in decision making about investments in new equipment that would help to reduce the pollution. Tutorial note: This topic will not be examined numerically.

#############
Output:
("entity"{tuple_delimiter}"Importance and Implementation of Environmental Management Accounting at Little Chemical Co"{tuple_delimiter}"cases"{tuple_delimiter}"The Little Chemical Co (LCC) faced significant fines and loss of customers due to excessive chemical emissions, prompting a need for better environmental management. The company’s management has recognized the importance of environmental management accounting (EMA) to address and manage environmental costs and impacts effectively. EMA provides both physical and monetary information, utilizing techniques like activity-based costing (ABC) to improve environmental performance and decision-making."){record_delimiter}
("entity"{tuple_delimiter}"Environmental management accounting"{tuple_delimiter}"concepts"{tuple_delimiter}"Environmental Management Accounting (EMA) involves the identification, collection, and analysis of both physical and monetary information related to environmental activities. It helps management make informed decisions by tracking the use of resources, waste generation, and environment-related costs, earnings, and savings."){record_delimiter}
("entity"{tuple_delimiter}"Environmental costs"{tuple_delimiter}"concepts"{tuple_delimiter}"Environmental costs refer to the expenses associated with a company's impact on the environment, including the consumption of resources, pollution control, and waste management. These costs can be categorized into conventional costs like resource usage, hidden costs embedded in overheads, contingent costs for future liabilities, and image costs related to environmental reputation. Additionally, environmental costs can be classified by their relation to quality, such as prevention, detection, internal failure, and external failure costs associated with managing environmental impacts."){record_delimiter}
("relationship"{tuple_delimiter}"Importance and Implementation of Environmental Management Accounting at Little Chemical Co"{tuple_delimiter}"Environmental management accounting"{tuple_delimiter}"The case of Importance and Implementation of Environmental Management Accounting at Little Chemical Co is related to Environmental management accounting."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Importance and Implementation of Environmental Management Accounting at Little Chemical Co"{tuple_delimiter}"Environmental costs"{tuple_delimiter}"The case of Importance and Implementation of Environmental Management Accounting at Little Chemical Co is related to Environmental costs."{tuple_delimiter}){record_delimiter}
#############################
Example 7:

Entity_types: ["concepts", "formulas", "methodologies", "quizzes", "features", "examples", "cases"]
Text:
Case: Life-Cycle Costing and Strategic Planning for Midhurst Co's New Air Conditioning Unit 
Midhurst Co manufactures air conditioning units and is considering an investment in a new unit that will be used in modern office buildings. Advances in technology mean that this unit is more sensitive to changes and variations in temperature and therefore it can regulate airflow and heating more efficiently. Midhurst Co's competitors currently do not have an equivalent product that can offer these features. Midhurst Co expects to sell 10,000 units over the predicted five-year life cycle of the unit. The finance director has just prepared the initial costings for the unit as follows: 
|                                     | $000    |
| Research and development costs      | 6,200   |
| Design costs                        | 33,450  |
| Marketing costs                     | 177,685 |
| Variable production cost per unit   | 42      |
| Fixed production cost               | 98,470  |
| Variable distribution cost per unit | 9       |
| Fixed distribution cost             | 10,300  |
| Variable selling cost per unit      | 4       |
| Fixed selling cost                  | 7,790   |
| Administration cost                 | 23,450  |
The finance director plans to use life-cycle costing to measure the profitability of the new product. The chief executive has asked for more information about life-cycle costing, as she is not sure whether it is the right method to use. The production director has reviewed the costings in detail and suggested a couple of changes. He is enthusiastic about the product and believes that modifications could be made to prolong the product's life but wonders when the best time would be to make changes to the product. 

Question 1. According to the life-cycle costing method, which TWO of the following statements regarding the stages of the life-cycle are true? A. At the introduction stage, further capital expenditure will be needed as production capacity will need to increase to meet demand B. The maturity stage occurs when the market has reached saturation point and bought enough of the product C. The majority of a product's life-cycle costs are determined by decisions which are made at the design and development stage D. The growth stage, when sales will have reached their peak and become stable, will be the most profitable stage 
Answer: 
The correct answer is A,C. Tutorial note: These statements are correct as capital expenditure is likely to increase at the introduction stage and the majority of a product's costs are determined at the outset. Reaching a saturation point defines the decline stage of the product lifecycle and stability defines the maturity stage. 

Question 2. What is the cost per unit for the new air conditioning unit using life-cycle costing (to the nearest $)? A.$35,740 B.$51,847 C.$88,390 D.$90,735
Answer: 
The correct answer is D. 
WORKINGS 
Cost per unit using life-cycle costing = Total cost over the full life-cycle of the product /Number of units to be produced over the life-cycle = $907,345,000/10,000 = $90,735 
*Total cost (in $000s) = $6,200 + $33,450 + $177,685 + ($42 * 10,000) + $98,470 + ($9 * 10,000) + $10,300 + ($4 * 10,000) + $7,790 + $23,450 = $907,345 

Question 3. The production director has suggested the following change for the costing of the new unit:
Currently material costs are 20% of the variable production costs per unit. One of the materials used is stainless steel which is budgeted at $2,000 per unit but an alternative corrosion-resistant metal costing 25% less can be used. The production director believes a 15% discount can be negotiated for the remainder of the materials.
What would be the revised material cost per unit (to the nearest whole $)?
Answer:
The correct answer is $ 6940 
WORKING 
Current variable material cost = 20% * $42,000 = $8,400 per unit 
Revised variable material cost = (85% * ($8,400 - $2,000)) + (75% * $2,000) = $6,940 

Question 4. The production director has also asked about the implications for production planning if the company wishes to extend the product's life-cycle. At what stage of the life-cycle is the unit most likely to undergo product development? A. Introduction B. Growth C. Maturity D. Decline 
Answer:
The correct answer is C. Tutorial note: Normally, product development occurs at the maturity phase in order to extend the profitable stage of the life-cycle. This is usually done by adding enhancements or new features. 

Question 5. The chief executive wants to be briefed on the advantages of using life-cycle costing. Which of the following statements relating to the advantages of life-cycle costing are correct? 1. It draws management's attention to all costs related to a product which other costing methods usually treat as period costs 2. It focuses on measuring a product's costs from concept to withdrawal rather than reviewing costs on a period by period basis 3. It focuses on what consumers are prepared to pay for a product and establishes cost budgets based on an expected selling price 4. It aids understanding of the relationship between decisions at the design stage and the cost of other functions, such as marketing A. 2, 3 and 4 only B. 1, 2 and 4 only C. 1 and 3 only D. 1, 2, 3 and 4 
Answer: 
The correct answer is B. Tutorial note: (3) is an advantage of target costing and not life-cycle costing. 
#############
Output:
("entity"{tuple_delimiter}"Life-Cycle Costing and Strategic Planning for Midhurst Co's New Air Conditioning Unit"{tuple_delimiter}"cases"{tuple_delimiter}"Midhurst Co is considering a new air conditioning unit investment that uses advanced technology to efficiently regulate airflow and temperature, offering a competitive advantage in the market. The company plans to use life-cycle costing to evaluate the unit's profitability, taking into account various costs including research, design, production, and marketing over the product's five-year life cycle. The production director suggests possible cost reductions and considers the timing for extending the product's life cycle, while the chief executive seeks to understand the benefits of life-cycle costing for strategic decision-making."){record_delimiter}
("entity"{tuple_delimiter}"Life-Cycle Costing"{tuple_delimiter}"concepts"{tuple_delimiter}"a system that tracks and accumulates the actual costs and revenues attributable to each product from development through to abandonment."){record_delimiter}
("entity"{tuple_delimiter}"Product Lifecycle Stages"{tuple_delimiter}"features"{tuple_delimiter}"The product lifecycle consists of five stages: development, introduction, growth, maturity, and decline. During the development stage, the product is designed, and manufacturing processes are established, with negative cash flow as no revenue is generated. As the product moves through the introduction, growth, and maturity stages, pricing strategies evolve to maximize demand and profits, while in the decline stage, demand and prices may decrease unless a niche market is found."){record_delimiter}
("entity"{tuple_delimiter}"Benefits of Life-Cycle Costing"{tuple_delimiter}"features"{tuple_delimiter}"Life-cycle costing helps management plan pricing strategies over the entire product lifecycle, leading to better cost control and understanding. By monitoring cumulative revenues and costs, it provides more meaningful information for decision-making than traditional period-based monitoring. Additionally, it allows for cost reduction during the design phase, improving profitability and informed decision-making on product development and continuation."){record_delimiter}
("relationship"{tuple_delimiter}"Life-Cycle Costing and Strategic Planning for Midhurst Co's New Air Conditioning Unit"{tuple_delimiter}"Life-Cycle Costing"{tuple_delimiter}"Life-Cycle Costing and Strategic Planning for Midhurst Co's New Air Conditioning Unit is related to Life-Cycle Costing."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Life-Cycle Costing and Strategic Planning for Midhurst Co's New Air Conditioning Unit"{tuple_delimiter}"Product Lifecycle Stages"{tuple_delimiter}"Life-Cycle Costing and Strategic Planning for Midhurst Co's New Air Conditioning Unit is related to Product Lifecycle Stages."{tuple_delimiter}){record_delimiter}
("relationship"{tuple_delimiter}"Life-Cycle Costing and Strategic Planning for Midhurst Co's New Air Conditioning Unit"{tuple_delimiter}"Benefits of Life-Cycle Costing"{tuple_delimiter}"Life-Cycle Costing and Strategic Planning for Midhurst Co's New Air Conditioning Unit is related to Benefits of Life-Cycle Costing."{tuple_delimiter}){record_delimiter}
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:"""

CONTINUE_PROMPT = "MANY entities were missed in the last extraction.  Add them below using the same format:\n"
LOOP_PROMPT = "It appears some entities may have still been missed.  Answer YES | NO if there are still entities that need to be added.\n"
