import streamlit as st 
from PIL import Image

st.title('Data Literacy📖')
st.subheader('Deconstructing Data Visualizations')
st.caption('10 minute read. For questions contact Jordan @ DataGovernance@perkinscoie.com')

st.subheader('Eyes on Data')

'Ever seen a brain teaser that looks like this?'
'List the color you see, not the word: __:orange[Purple] :violet[Green] :blue[Blue] :green[Red] :red[Green] :blue[Orange] :red[Red]__'

'Can you do it easily? Or does your brain try to trick you? What you expect to see might affect your ability to interpret what you ___actually___ see!'

'Keeping with the colorful examples, let’s say you are interested in the favorite colors of people on your team. You ask around and come up with this list:'
'Purple Purple Purple Purple Purple Green Green Green Green Green Green Green Green Blue Blue Blue Blue Blue Blue Red Red Red Red Red Red Red Red Red Orange Orange Orange Orange'
'With only two lines of text, it probably wouldn’t take you too long to count each color. There’s nothing necessarily distracting or confusing within these two lines of text. You could even make a list and note that there are 5 purples, 8 greens, 6 blues, 9 reds, and 4 oranges.'
'But what if you want a better way to understand and communicate the same information? Enter, __data visualization__. Imagine you’re presented with this:'

# [Chart]

'How much faster and easier was it for you to pull the insights out of this graphic versus the string of words? (Psst – do you notice anything that can be improved with this chart? Keep reading to see if you’ve spotted it as we break this apart together!)'
'__Data Visualization__ can be a fantastic way to __quickly and clearly communicate a story with data__. This might help you __share your data__ in a memorable way, or __emphasize a particular point__. And if you’re analyzing data, a data visualization might help you __identify new insights__ from your data, like patterns or outliers.'

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

'But without __thoughtful design__ and __accurate data__, a visualization may be misleading. Like the :orange[Purple] :violet[Green] :blue[Blue] brain teaser, a visualization might be intentionally designed to mislead. (Ever have a Facebook friend share an infographic that makes you pause?) But a visualization might be accidentally misleading, with a poor use of visuals or too much clutter.'
'Today we’ll explore tips to break down data visualizations so you can be __confident in your use and interpretation of visuals__. Let’s get started!'

st.subheader('Eyes on Data: Deconstructing Visualizations')

# [Image - Sample Visualization] 

'Recall the chart presented above with the data about favorite colors. Let’s add a scenario to this chart and walk through it together.'
'___THE SCENE: The firm Data Dan & Associates is undergoing a rebrand. As part of this rebrand, they want to change their current color scheme. Visual Valerie is contracted to lead the rebrand for Data Dan, starting with a new logo. After lots of research into the culture and values of the firm, she unveils her pitch for a new logo to a team of stakeholders.___'
'___“Red would be the perfect color for your logo!” she claims, showing a few dazzling graphics displaying her recent research. You are a stakeholder hearing Valerie’s pitch. Before casting your vote, you want to take a closer look.___'
'By __identifying context, interpreting the data, and examining the visual components__, we will be able to draw our own conclusions about Visual Valerie’s pitch.'

st.subheader('Step One: Identify the Context')
# [Image - Sample Visualization, Context Zoom] 

'First, look at the surrounding __context__. What __role__ does this visualization play -- are you being ___persuaded___ of something? Is this visualization being used to ___support a conclusion___? Is it ___summarizing data___, or adding something new into the conversation?'
'In this example, Visual Valerie is persuading you to adopt the logo design. She designed the presentation and supporting data for this purpose, with you as the target audience.'

st.subheader('Step Two: Interpret the data')

'Next, try to __interpret__ the data being used. ___Where and who___ does this data come from? Do you trust the source?'

# [Image – Data behind Viz] 

'You’ve already identified the context and understand that the Visual Valerie is hoping to convince you to adopt her logo. Do you think this is a ___complete___ set of data? Do you trust the way she collected this data? Do you trust the way she presented the data?'

st.expander('Expander')
with st.expander('Deceiving Data Depictions: The Story of the Datasaurus'):
  'In past data literacy modules, you’ve learned to describe data using mean, median, and correlation. A data visualization might paint a different picture of your data – literally.'
  'Data scientists mapped 12 __wildly__ different datasets having the same mean, median, and correlation. Even though these three summary statistics are the same, check out just how different the visualizations are below:'
# https://redirect.viglink.com/?format=go&jsonp=vglnk_169723894958410&key=949efb41171ac6ec1bf7f206d57e90b8&libId=lnp88yqf01021u9s000UA4u49hwcb&loc=https%3A%2F%2Fwww.r-bloggers.com%2F2017%2F05%2Fthe-datasaurus-dozen%2F&v=1&out=https%3A%2F%2Fwww.autodeskresearch.com%2Fpublications%2Fsamestats&ref=https%3A%2F%2Fwww.bing.com%2F&title=The%20Datasaurus%20Dozen%20%7C%20R-bloggers&txt= 

st.subheader('Step Three: Scan for Effective Visuals')

'Finally, put on your artist hat and think about the __visuals__ being used. It the visual ___easy to read___? Is everything ___clearly and accurately labeled___? Is anything ___hidden or obscured___?'

'You don’t have to be a data visualization expert – nor an art critic – to determine if a visual is effective.'

st.subheader('___Format___')
'Starting at the broadest point – the __chart style__ itself. Ask, is this the best format to display this information?'

# [Image – Chart Types]

'Maybe it’s the right chart or graphic for the dataset, but there are too many fields being used. Or perhaps it’s simply the wrong chart – for example, you would expect a pie chart to represent a “parts of a whole” relationship.'

st.expander('Expander')
with st.expander('Dive deeper: Choosing the right chart'):
  'If you’re constructing data visualizations, here’s a great flow chart to set you on the right track.'
# chart-chooser-2020.pdf (typepad.com) 

st.subheader('___Colors___')

'At the start of this module, you saw this as part of the brain teaser: :green[Red] :red[Green].'
'What if, instead of color names, it read: :green[No] :red[Yes]. Or :green[Stop] :red[Go]? Your color choice may imply certain outcomes or concepts.'

'__High contrast__ in colors might similarly trick your brain into thinking there’s a bigger difference between variables than might actually be present. Think about a heat map of the weather where you see bright red and sunny yellow. If you’re expecting the bright red weather region to be around 100 degrees, you’d think the yellow weather would imply a much lower (but still warm) temperature. It would be misleading to have the yellow region represent freezing weather, or very hot weather.'

# [Image with weather example] 

st.subheader('___Scales and Labels___')

'Another mistake in data visualization is assigning __labels and scales__ that are ___inconsistent___ with the data. Is there a big jump between numbers that isn’t clear?'

# [Chart with bar lines too close together or too far apart] 

'Are the axes clearly labeled so the audience can tell what they are supposed to read?'

'To learn more about visual elements, look here: Data visualization: A view of every Points of View column : Methagora (nature.com)'

st.subheader('All in all...')

'Deconstructing data visualizations means slowing down to digest what you’re actually seeing. Do you find Visual Valerie’s logo pitch convincing? Maybe, maybe not – but now you know that decision is in your hands, and you were able to interpret all the data on your own.'
st.divider()
st.subheader('Data Dan’s Questions to Ask:')
'1. Am I being persuaded of anything?'
'2. Do I trust the data behind the visualization?'
'3. Do I have the context to interpret this information?'
'4. Is this the correct format to display this information? Is anything hidden or obscured?'
st.divider()
st.subheader('Data Visualization Resources')

'Want to learn more about Data Visualization at the firm? Check out Data Visualization Resources on Connections.'
'Ready to build your own data visualization? Check out this introductory video to PowerBI and more on LearningSite: Power BI 101 Video. Reach out to the Data Visualization team to join the PowerBI community.'
'Other questions about Data Visualization? Please contact Bennie @ BLopez@perkinscoie.com.'
'Thanks for following along! If you have any questions about this module or past data literacy content, please email Jordan @ DataGovernance@perkinscoie.com.'
