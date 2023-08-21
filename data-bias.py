import streamlit as st

# from location import Image

st.title('Data Literacy📖') 
st.subheader("Making Inferences: Accounting for Bias")
st.caption("10 minute read. For questions contact Jordan @ DataGovernance@perkinscoie.com")

'Meet Data Dan, your new Data Literacy pal! Keep your eyes peeled for tips and tricks from Data Dan as you continue on your adventure in data literacy.'
# image st.image(Data-Dan.png)
''
'Data bias is all around us.'
''
'___What is data bias?___ We say data is biased when humans bake preconceived notions (whether consciously or not) into the collection, analysis, or reporting of data. Data bias typically occurs for two reasons: (1) __a logical fallacy__ (e.g., availability bias) and/or (2) a dataset that is __not representative of the population__ (e.g., sampling or non-response bias). This might be due to an error in how the data was collected or analyzed.'
''
'___Why is data bias a problem?___ Data bias can lead to __inaccurate, unhelpful, or problematic results__! We use data to make lots of decisions, ¬from budgeting, to hiring, to measuring client engagement and satisfaction. Data-based insights are a critical component of our business! Being aware of common biases helps ensure we are measuring what we aim to measure, and that our inferences are sound.'
''
st.expander('Expander') 
with st.expander('Did you know?'): 
    st.write('One concern about artificial intelligence is its ability to perpetuate bias. Check out this article: https://www.weforum.org/agenda/2021/07/ai-machine-learning-bias-discrimination/')
''
'Today we are going to look through our telescope at the universe of data bias. Follow Data Dan as we explore three spaces you may encounter bias: in data collection, in analytics, and in machine learning.'
st.subheader('Station 1: Data Collection')
''
'Landing at our first station…let’s look at the first area where we might see data bias: during collection. Here we are interested in how survey questions are phrased, who is included in the response group, and how responses are collected. Let’s take a closer look.'
''
'---'
'__Selection Bias__ occurs when the sample was collected in an inaccurate or biased way.'
st.divider()
''
'This might happen if we sample a __non-representative group__! Let’s say we want to know how many business professionals at the firm have pets. If we only survey business professionals who have joined our Perkins Pet Parents resource group, it is highly likely that we will overestimate the number of total business professionals who have pets. Look closely at __who__ data is being collected from.'
''
'__Sampling Bias__ is a common type of selection bias. Sampling bias occurs when certain people in the population are more likely to be selected than others. This can happen when respondents are not picked completely at random. A common example of this is found in surveys conducted by landline phones. Because most people with landlines are older, the results are more likely to be biased towards the perspective of older people.'
''
##':red[(Learn more about how to analyze sampling here: LINK TO OTHER COMM)]'
''
'Imagine you’re surveying your colleagues on if they drink coffee. You stand outside the coffee machine to survey 30 people. Think about who might cross your path: coffee drinkers! Remember: you want your sample to reflect the ___entire___ group you are reporting on!'
''
'Another example of this you might find out in the wild is in the world of online reviews. In my observation, those most likely to leave an online review are those who have either (1) had a ___terrible___ experience; or (2) had a great experience ___and___ are the type to leave a review. The experience ___you___ are likely to have is somewhere in the middle. Do you also take online reviews with “a grain of salt?”'
''
'Phew! Now you know how to evaluate sampling methods. Now let’s make sure we asked questions in a fair way.'
''
st.text('__Response Bias__ occurs when participants respond to a questionnaire in a way that does not reflect their actual needs or beliefs.')
'Why would they do this? Perhaps the right answer wasn’t an option. For example, you hand me a survey asking if I like Diet Dr. Pepper, but I’ve never tried it. The options were “yes”, “no” and “neutral”. I’m not neutral – the right answer would be “I don’t know!” – but I select “neutral” anyway. This might also occur when “prefer not to answer” is an option on a survey.'
''
'This type of bias also occurs if respondents feel they are being “watched” or “judged” for their responses. Imagine you receive a survey, and there is this question: “Do you believe, as most Americans do, that employers should provide pet insurance free of charge?” Now imagine you were asked this question in person or over the phone. Studies show that when surveyed in this way, most people will try to answer in a way they think is the most socially acceptable.'
''
'__If you receive a report from which you want to make decisions (i.e., infer meaning)__, take a tip from Data Dan and ask…'
'1. How was the data collected? If by a questionnaire or survey, were the questions phrased in a neutral way? Were respondents given the chance to respond accurately?'
'2. Who is represented in the data? If using a sample to generalize about a population (e.g., the entire firm), have you checked that the sample fairly and accurately represents the population you want to learn about?'
''
':red[__Apply it!__]✍️'
##Identify the possible bias.
st.text('The office is abuzz about a new study that came out saying that 60% of law firm employees love reading. You look closer at the study and find the options for response were “I love to read” “I like to read” and “prefer not to answer”.')
st.text('What bias does this represent?')
'Answer:' 
'1. Selection Bias – Try again!'
'2. Response Bias – Correct! The options are limited in a way where participants might select the answer that does not reflect their true beliefs.'
'3. Sample Bias – Try again!'
''
'We’ve seen how bias might creep into our  data collection. Next, let’s look at how bias can affect our interpretation and use of data.'
''
st.subheader('Station 2: Analytics')
'Up, up, and away to our next stop…analytics! Data bias can manifest itself in how we report out and analyze data.'
''
st.divider()
'__Reporting Bias__ happens when certain data is withheld from an analysis.'
st.divider()
'Let’s imagine you are handed a report looking at how our workforce has grown over the past five years. The report shows a count of all the new hires for each month. It looks like our population has exploded: 10 new hires in March, 25 in April, 15 in May… We know the data is accurate, but can you spot the bias?'
''
'If you answered “data is being withheld from this report”, you’re right! You’re missing information on departures or movement around the firm – critical context to the actual “growth” shown in this report.'
''
'Another example of reporting bias to watch out for is called “data fishing.” Data fishing happens when the researcher has a result they expect or want to see, so they look only for the data that confirms that result. To counteract this: if you are doing the analysis, make sure you have your research question and methods defined before you start gathering data. If you find yourself deviating from that plan because you are not getting the result you want, you may fall victim to data fishing. To counteract data fishing as a report-receiver, ask if any data was excluded from the results and, if so, why?'
''
'__If you receive a report you hope to use as evidence in your decision-making__, take a tip from Data Dan and ask…'
'1. Is there any data being withheld? Why?'
'2. Does the data support the question being asked?'
'3. What do I expect to see in this data? Is that affecting my analysis?'

'We’ve talked about data bias in how information is collected and analyzed. Now what about bias in systems?'
''
st.subheader('Station 3: Machine Learning')
''
'In a galaxy far, far, away…or right at your fingertips. What happens when our systems and machines are biased? How can we tell?'
''
'You may have heard the common saying in the data world: “garbage in, garbage out”. For our AI or machine learning, this means that the machine learning is only as good as the data it is trained upon. There are a few sources of potential bias in systems. Today we’re going to focus on only one…'
''
st.divider()
'__System Drift__ occurs when the definition of a term changes over time.'
st.divider()
''
'(Psst – this doesn’t just happen in machine learning, but in all of our business operations.) Let’s say we are running a report on the types of pets we cover under our pet insurance plans.. Five years ago, our plans only covered cats and dogs. Today, we cover all kinds of animals¬: “snakes”, “rabbits”, “gerbils”. The meaning has changed from “only cats and dogs” to “all domesticated animals living in your home”.'
''
'Not to sound biased…but this is a reason data governance is important! (You can find the meanings of common business terms and acronyms at the firm using our data catalog, Collibra.) If we maintain and organize our data, we reduce the possibility for system drift. This makes our data more accurate and reliable.'
''
'__If you’re getting information from a machine__, take a tip from Data Dan and ask…'
'1. How are each of the data fields defined? Have those definitions changed over time?'
'2. How is the quality of the data ensured?'
'3. Can I see, in plain language, how the model was trained? Do I notice any biased logic in the way the model was trained?'
'4. After answering the questions above, can I trust this result?'
''
'3…2…1…blast off! Now that you’re able to spot data bias, you can be more confident your data-backed decisions.'
''
if st.button('🌟You are a data star!🌟'): 
    from streamlit_extras.let_it_rain import rain     
    rain( 
        emoji="🌟", 
        font_size=54, 
        falling_speed=5, 
        animation_length="short", 
        )
''
'This material is unquestionably complex. You do not need to be an expert in these topics. Simply knowing which questions to ask can help you make better decisions with data. If you want a second pair of eyes, reach out to your Data Governance team!'
'You’re ready to take off! Thank you for following along on this month’s module as we explored the universe of bias. You’re out of this world!'
