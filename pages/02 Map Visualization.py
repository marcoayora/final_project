import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Tableau Graph Visualizations", page_icon=":world_map:", layout="wide")
# Everyone should insert their code of Tableau in here to make it Unique! The tableau Temp should be inside a main function:
st.title ("Barcelona Map Divided by Neighboorhoods/Districts Interactive Dashboard")
st.markdown("*With Tableau*")
def main():
    html_temp='''<div class='tableauPlaceholder' id='viz1701914627545' style='position: relative'><noscript><a href='#'><img alt='Map Visualizations ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ZM&#47;ZM6XH2ZGW&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;ZM6XH2ZGW' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;ZM&#47;ZM6XH2ZGW&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='es-ES' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1701914627545');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='827px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>'''
    components.html(html_temp, width=1100, height=800)

if __name__ == '__main__':
    main()