import streamlit as st 
from PIL import Image

st.title('Data Literacy📖')
st.subheader('Deconstructing Data Visualizations')
st.caption('10 minute read. For questions contact Jordan @ DataGovernance@perkinscoie.com')

st.subheader('Eyes on Data')

'Ever seen a brain teaser that looks like this?'
'List the color you see, not the word: Purple Green Blue Red Green Orange Red'

'Can you do it easily? Or does your brain try to trick you? What you expect to see might affect your ability to interpret what you actually see!'

'Keeping with the colorful examples, let’s say you are interested in the favorite colors of people on your team. You ask around and come up with this list:'
'Purple Purple Purple Purple Purple Green Green Green Green Green Green Green Green Blue Blue Blue Blue Blue Blue Red Red Red Red Red Red Red Red Red Orange Orange Orange Orange'
'With only two lines of text, it probably wouldn’t take you too long to count each color. There’s nothing necessarily distracting or confusing within these two lines of text. You could even make a list and note that there are 5 purples, 8 greens, 6 blues, 9 reds, and 4 oranges.'
'But what if you want a better way to understand and communicate the same information? Enter, data visualization. Imagine you’re presented with this:'

# [Chart]

'How much faster and easier was it for you to pull the insights out of this graphic versus the string of words? (Psst – do you notice anything that can be improved with this chart? Keep reading to see if you’ve spotted it as we break this apart together!)'
'Data Visualization can be a fantastic way to quickly and clearly communicate a story with data. This might help you share your data in a memorable way, or emphasize a particular point. And if you’re analyzing data, a data visualization might help you identify new insights from your data, like patterns or outliers.'

st.expander('Expander')
with st.expander('When might you want to use a data visualization?'):
  if st.checkbox("a. To summarize your data."):
    st.write('Partially correct, keep going.')
  if st.checkbox("b. To communicate data with a broader audience."):
    st.write('Partially correct, keep going.')
  if st.checkbox("c. To make or emphasize a point in research or presentations."):
    st.write('Partially correct, keep going.')
  if st.checkbox("d. All of the above!"):
    st.write('Correct! Data visualizations can be used to summarize, communicate, or emphasize data.')

'But without thoughtful design and accurate data, a visualization may be misleading. Like the Purple Green Blue brain teaser, a visualization might be intentionally designed to mislead. (Ever have a Facebook friend share an infographic that makes you pause?) But a visualization might be accidentally misleading, with a poor use of visuals or too much clutter.'
'Today we’ll explore tips to break down data visualizations so you can be confident in your use and interpretation of visuals. Let's get started!'

st.subheader('Eyes on Data: Deconstructing Visualizations')

# [Image - Sample Visualization] 

'Recall the chart presented above with the data about favorite colors. Let's add a scenario to this chart and walk through it together.'
'THE SCENE: The firm Data Dan & Associates is undergoing a rebrand. As part of this rebrand, they want to change their current color scheme. Visual Valerie is contracted to lead the rebrand for Data Dan, starting with a new logo. After lots of research into the culture and values of the firm, she unveils her pitch for a new logo to a team of stakeholders.'
'“Red would be the perfect color for your logo!” she claims, showing a few dazzling graphics displaying her recent research. You are a stakeholder hearing Valerie’s pitch. Before casting your vote, you want to take a closer look.'
'By identifying context, interpreting the data, and examining the visual components, we will be able to draw our own conclusions about Visual Valerie’s pitch.'

st.subheader('Step One: Identify the Context')
# [Image - Sample Visualization, Context Zoom] 

'First, look at the surrounding context. What role does this visualization play -- are you being persuaded of something? Is this visualization being used to support a conclusion? Is it summarizing data, or adding something new into the conversation?'
'In this example, Visual Valerie is persuading you to adopt the logo design. She designed the presentation and supporting data for this purpose, with you as the target audience.'

st.subheader('Step Two: Interpret the data')

'Next, try to interpret the data being used. Where and who does this data come from? Do you trust the source?'

# [Image – Data behind Viz] 

'You've already identified the context and understand that the Visual Valerie is hoping to convince you to adopt her logo. Do you think this is a complete set of data? Do you trust the way she collected this data? Do you trust the way she presented the data?'

st.expander('Expander')
with st.expander('Deceiving Data Depictions: The Story of the Datasaurus'):
  'In past data literacy modules, you’ve learned to describe data using mean, median, and correlation. A data visualization might paint a different picture of your data – literally.'
  'Data scientists mapped 12 wildly different datasets having the same mean, median, and correlation. Even though these three summary statistics are the same, check out just how different the visualizations are below:'
# https://redirect.viglink.com/?format=go&jsonp=vglnk_169723894958410&key=949efb41171ac6ec1bf7f206d57e90b8&libId=lnp88yqf01021u9s000UA4u49hwcb&loc=https%3A%2F%2Fwww.r-bloggers.com%2F2017%2F05%2Fthe-datasaurus-dozen%2F&v=1&out=https%3A%2F%2Fwww.autodeskresearch.com%2Fpublications%2Fsamestats&ref=https%3A%2F%2Fwww.bing.com%2F&title=The%20Datasaurus%20Dozen%20%7C%20R-bloggers&txt= 

st.subheader('Step Three: Using Effective Visuals')

'Finally, put on your artist hat and think about the visuals being used. It the visual easy to read? Is everything clearly and accurately labeled? Is anything hidden or obscured?'

'You don’t have to be a data visualization expert – nor an art critic – to determine if a visual is effective.'

st.subheader('Format')
'Starting at the broadest point – the chart style itself. Ask, is this the best format to display this information?'

# [Image – Chart Types]

'Maybe it’s the right chart or graphic for the dataset, but there are too many fields being used. Or perhaps it’s simply the wrong chart – for example, you would expect a pie chart to represent a “parts of a whole” relationship.'

st.expander('Expander')
with st.expander('Dive deeper: Choosing the right chart'):
  'If you're constructing data visualizations, here’s a great flow chart to set you on the right track.'
# chart-chooser-2020.pdf (typepad.com) 

st.subheader('Colors')

'At the start of this module, you saw this as part of the brain teaser: Red Green.'
'What if, instead of color names, it read: No Yes. Or Stop Go? Your color choice may imply certain outcomes or concepts.'

'High contrast in colors might similarly trick your brain into thinking there’s a bigger difference between variables than might actually be present. Think about a heat map of the weather where you see bright red and sunny yellow. If you’re expecting the bright red weather region to be around 100 degrees, you’d think the yellow weather would imply a much lower (but still warm) temperature. It would be misleading to have the yellow region represent freezing weather, or very hot weather.'

# [Image with weather example] 

st.subheader('Scales and Labels')

'Another mistake in data visualization is assigning labels and scales that are inconsistent with the data. Is there a big jump between numbers that isn’t clear?'

# [Chart with bar lines too close together or too far apart] 

'Are the axes clearly labeled so the audience can tell what they are supposed to read?'
'To learn more about visual elements, look here: Data visualization: A view of every Points of View column : Methagora (nature.com)'

'All in all...'

'Deconstructing data visualizations means slowing down to digest what you’re actually seeing. Do you find Visual Valerie’s logo pitch convincing? Maybe, maybe not – but now you know that decision is in your hands, and you were able to interpret all the data on your own.'
st.divider()
st.subheader('Data Dan's Questions to Ask:')
# Am I being persuaded of anything?
# Do I trust the data behind the visualization?
# Do I have the context to interpret this information?
# Is this the correct format to display this information? Is anything hidden or obscured? 
st.divider()
st.subheader('Data Visualization Resources')

'Want to learn more about Data Visualization at the firm? Check out Data Visualization Resources on Connections.'

'Ready to build your own data visualization? Check out this introductory video to PowerBI and more on LearningSite: Power BI 101 Video. Reach out to the Data Visualization team to join the PowerBI community.'

'Other questions about Data Visualization? Please contact Bennie @ BLopez@perkinscoie.com.'

'Thanks for following along! If you have any questions about this module or past data literacy content, please email Jordan @ DataGovernance@perkinscoie.com.'
