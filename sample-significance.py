import streamlit as st 
from PIL import Image

st.title('Data Literacy📖')
st.subheader('Making Inferences: Sampling and Significance')
st.caption('10 minute read. For questions contact Jordan @ DataGovernance@perkinscoie.com')
data_dan = Image.open('data-dan-intro.png')
st.image(data_dan)

'As you have followed along with the data literacy program, you’ve learned to describe, analyze, and question data. In this module, you’ll learn to __make and evaluate inferences__.'
st.expander('Expander') 
with st.expander('Tell me more about inferential statistics!'): 
    st.write('There are two types of statistics: (1) __descriptive__ statistics and (2) __inferential__ statistics. Descriptive statistics describe an ___entire___ set of data. Inferential statistics look ___only at a sample___ to make a conclusion about the population. For example, you survey 200 employees on their preferences for remote work, and use their responses to infer that the whole firm would, on average, respond the same way. The 200 employees would be your sample, and you would draw a conclusion about the whole firm (the population).')
'Grab your detective hat, today it’s time to join Data Dan and sleuth out some statistics.'
detective_dan = Image.open('detectivedan.png')
st.image(detective_dan)
'Like a detective sorts through evidence to paint a bigger picture, a data analyst might conduct research to make inferences about their area of study. A data analyst might use a __sample to draw inferences about a population__.'
'Can we trust all the inferences we hear? Can we actually infer ___anything___ from our data?'
'There are two main suspects carrying the secret to the strength of our inferences: __sample size__ and __significance__. Help Data Dan investigate...'
st.subheader('Suspect 1: Sampling')
'Let’s talk sampling.'
'First, __what is a sample__? A ___sample___ describes a portion of the population from which data is collected. The ___population___ is the __whole__ group being studied.'

# image st.image(Sample-Pop.png) 

st.expander('Expander') 
with st.expander('Key Terms from Data Dan'): 
    st.write('__Population__: the whole group or area of interest.')
    st.write('__Sample__: a portion of the population from which data is collected.')
    st.write('__Inference__: A conclusion about a population, drawn only from a sample.')

'Mrs. Peacock, Professor Plum, Mr. Green, Colonel Mustard. Just like we need to figure out our key suspects, we need to determine __who__ is in our population. Are we interested in everyone in the firm? Just business services? Just attorneys? All law firm employees in the world? '

st.expander('Expander')
with st.expander(':red[__Apply it!__]✍️'):
    '80% of U.S. remote workers say they work better at home.'
    st.text('What’s the population?')       
    if st.checkbox("A. Remote workers"):
        st.write('Close, but not quite. Is there a more precise option for the population?')
    if st.checkbox("B. Remote workers in the United States"):
        st.write('Correct! Great job!')
    if st.checkbox("C. All workers in the United States"):
        st.write('Close, but not quite. Is there a more precise option for the population?')
    if st.checkbox("D. All US Citizens"):
        st.write('Close, but not quite. Remember, the population isn’t necessarily the largest group.')

'___Great job! Now that we know how to find the population, can you determine who should be sampled?___'
'Remember, your sample is a ___portion of the population___ from whom you are collecting data.'
'Let’s say you’re asked to restock the vending machine in the Chicago office. To do so, you want to determine the favorite beverages in the office. Who is in your sample? Would you ask your colleague in Seattle? What about your colleague who works remotely, but is based in Chicago? If you’ve answered no to both of these, you’re correct! We want the sample to reflect the population.'

sample_pop = Image.open('sample-population.png')
st.image(sample_pop)

'Now, can you distinguish between the population and the sample?'

st.expander('Expander')
with st.expander(':red[__Apply it!__]✍️'):
    'The Data Governance Team surveys a random sample of 50 Perkins business professionals to see if the business professionals are enjoying the data literacy content.'
    st.text('Identify the population and the sample.')
    if st.checkbox("a. The population is the entire firm, the sample is all Perkins business professionals."):
        st.write('Not quite. We cannot draw inferences about the entire firm because they were not represented in the sample.') 
    if st.checkbox("b. The population is all business professionals working at law firms, the sample is Perkins business professionals."):
        st.write('Not quite. We cannot draw inferences about business professionals in all firms because only Perkins business professionals were sampled.')
    if st.checkbox("c. The population is all Perkins business professionals, the sample is the 50 business professionals surveyed."):
        st.write('Correct! Great job! You are interested in business professionals, and you sampled business professionals.')
    if st.checkbox("d. The population is everyone in the world, the sample is the 50 business professionals surveyed."):
        st.write('Not quite. We cannot draw inferences about the entire world because they were not represented in the sample.')

'Now you know who should have been sampled. How do you make sure the sample is fair?'

st.subheader('To accurately represent the population, samples must be random.')

# image st.image(random-sample.png) 

'Randomized samples help reduce possible bias. Imagine you’re surveying your colleagues on if they drink coffee. You stand outside the coffee machine to survey 30 people. Think about who might cross your path: you’re more likely to catch coffee drinkers on their way to get their next cup! You want your sample to fairly reflect the population.'

st.expander('Expander')
with st.expander(':red[__Apply it!__]✍️'):
    'You want to estimate the percentage of the entire firm that has volunteered in the last month.'
    st.text('Which approach would give you a fair sample?')
    if st.checkbox("Randomly selecting office numbers and surveying each person."):
        st.write('Not quite. Your sample would only include people with offices – you would miss remote workers.') 
    if st.checkbox("Surveying the entire technology department."):
        st.write('Not quite. Your sample would only reflect the technology department, not the entire firm.')
    if st.checkbox("Randomly selecting names from the distribution list for all attorneys."):
        st.write('Not quite. Your sample would only include attorneys.')
    if st.checkbox("All of the above."):
        st.write('Not quite. Click on each answer to see why in more detail.')
    if st.checkbox("None of the above."):
        st.write('Correct! Great job! None of the options give you a random sample that would reflect the entire firm. Remember, samples need to appear as close to the population as possible.')

st.expander('Expander')
with st.expander('Let’s take this one step further. 👉 How big should my sample be?'):
    'If a sample size is ___too small___, you run the risk of inaccurate results. '
    'If a sample size is ___too big___, you might needlessly waste time and resources. '
    'How do we get the sample size ___just right___?'
    'You can calculate the sample size needed with the confidence level and the margin of error. There are many calculators online to do this, such as this one: https://www.calculator.net/sample-size-calculator.html'

st.divider()
st.subheader('Be a sampling sleuth!')
'Ask these questions to assess whether you have a strong sample:'
'1. Who was sampled?'
'2. Who was excluded?'
'3. How was the sample collected? Was it random?'
st.divider()

'___Great job! You learned the difference between sample and population, and how to identify if a sample is representative of the population.___'

st.subheader('Suspect 2: Significance')

'What does it ___really___ mean when someone says a result is "significantly higher" or "significantly lower"?'

'__Significance__ (or the p-value) is the probability of a result occurring by chance, not due to the causal relationship you’re studying.'
'Essentially, significance level is a way of measuring the ___reliability___ of the data. How strong is your inference?'

'The __lower the p-value__, the __stronger the inference__ you can make. You may see this number set at 0.05% or 0.01%. When reviewing reports, keep an eye out for p-value. The person presenting the data should always show this number, especially if they are trying to prove a causal relationship.'

st.expander('Expander') 
with st.expander('Key Terms from Data Dan'): 
    st.write('__Significance__: the likelihood of an event occurring by chance.')
st.divider()
st.subheader('Be a significance sleuth!')
'Ask these questions to assess whether you have a strong sample:'
'1. Did the presenter include the significance value (p-value?) If so, does it support the inference the presenter wants us to make?'
'2.  Did the presenter include information on the size of the population, the size of the sample, and how they drew their sample? Is that sample randomly drawn? Is the sample a large enough size?'
'3. Am I able to view the statistics supporting this inference?'
st.divider()
# st.image(significance.png) 
''
st.header('Case closed…or not?')
'Trust your gut! When you have questions about a finding, don’t be afraid to dive deeper.'
''
'You’re all set! Have fun making and analyzing inferences. See you next month with Data Dan.'

if st.button('🌟You are a statistical sleuth!🌟'): 
    from streamlit_extras.let_it_rain import rain     
    rain( 
        emoji="🌟", 
        font_size=54, 
        falling_speed=5, 
        animation_length="short", 
        )

