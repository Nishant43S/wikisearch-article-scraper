import streamlit as st
from streamlit_option_menu import option_menu
import wikipedia
import time
import requests
import base64
### importing libraries

## main logic
def wiki_search(search)->str:
    ### writing main logicb in try except block
    try:
        result = wikipedia.summary(
            title=search,chars=32,
            sentences=10
        )
        return result
    except Exception as err:
        st.info("Something Wrent wrong...")
        st.warning(err)

def check_internet_connection():
    try:
        # Attempt to make an HTTP GET request to a reliable site
        response = requests.get("https://www.google.com", timeout=5)
        # Check if the request was successful (status code 200)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
    except requests.Timeout:
        return False
check_internet_connection()


st.set_page_config(
    page_icon="📰",page_title="Wiki Search",   # setting the page layout
    initial_sidebar_state="collapsed",
    layout="centered"
)

## creating sidebar

Sidebar = st.sidebar

with Sidebar:
    st.title("Developer: Nishant Maity")
    Menu = option_menu(
        menu_title="Menu",
        menu_icon="📰",
        options=["Wiki Search","App info"],
        icons=["card-text","info"]
    )
    st.header("Social Links")

    st.markdown(
        """
        <ul type="none">
            <li class="list"><a class="link" href="https://github.com/Nishant43S" target="_main">Github</a></li>
            <li class="list"><a class="link" href="https://www.instagram.com/invites/contact/?igsh=18v15zzwabz7i&utm_content=m95jbmo" target="_main">Instagram</a></li>
        </ul>
        """,unsafe_allow_html=True
    )

    def external_css(css_file): # attaching external css file
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

    
    if __name__=="__main__":
        external_css("style.css")
    

## main app

if Menu == "Wiki Search":
    def Wikisearch():
        st.title("Wiki Search")

        st.write("find wikipedia articles 📑 with this app view project on [github](https://github.com/Nishant43S/wikisearch-article-scraper.git). to create this types of app visit this website [streamlit](https://docs.streamlit.io/get-started).")


        Input_form = st.form(key="Input Form",clear_on_submit=False,border=False)
        with Input_form:
            Search_item = st.text_input(
                label="Search Article",label_visibility="visible",
                type="default"
            )

            Submit_btn = st.form_submit_button(
                label="Generate Article"
            )

        if Submit_btn:
            if Search_item.strip() == "":
                st.warning("Write Something...")
            else:

                if __name__=="__main__":

                    output = wiki_search(search=Search_item)
                    st.write(f"Article on {Search_item}")
                    with st.spinner("Generating"):
                        time.sleep(3)

                    def stream_data():   ### output animation
                        for word in output.split(" "):
                            yield word + " "
                            time.sleep(0.02)
                    st.write_stream(stream=stream_data)

                    Article_download = output

                    # Function to generate download link button
                    def create_download_link(text, filename=f"{Search_item}.txt"):
                        try:
                            b64 = base64.b64encode(text.encode()).decode()  # Encode the text to base64
                            href = f'<a style="text-decoration: none; color: white; text-transform: uppercase; letter-spacing: 0.1em;" class="Btn" href="data:file/txt;base64,{b64}" download="{filename}">Download Article</a>'
                            return href
                        except :
                            st.info("something went wrong")

                    # Display the download link directly
                    st.markdown(create_download_link(Article_download), unsafe_allow_html=True)
                    

                    st.write("---")

                    st.header("Article Summary")

                    try:
                        with st.spinner("Generating summary..."):
                            article = wikipedia.page(Search_item)  ### article long summary
                            article_title = article.title
                            article_url = article.url
                            article_summary = article.summary

                            st.write(f"Title: {article_title}")
                            st.text("")
                            st.write(article_summary)

                            summary_download = article_summary

                            # Function to generate download link button
                            def create_download_link1(text, filename=f"{Search_item}-summary.txt"):
                                try:
                                    b64 = base64.b64encode(text.encode()).decode()  # Encode the text to base64
                                    href = f'<a style="text-decoration: none; color: white; text-transform: uppercase; letter-spacing: 0.1em;" class="Btn" href="data:file/txt;base64,{b64}" download="{filename}">Download Summary</a>'
                                    return href
                                except :
                                    st.info("something went wrong")

                            # Display the download link directly
                            st.markdown(create_download_link1(summary_download), unsafe_allow_html=True)
                            st.link_button("visit on article",url=article_url)


                    except:
                        st.info("something went wrong...")
                    st.write("---")

                    st.subheader("Similar searches-")
                    try:
                        Similar_search = wikipedia.search(Search_item)

                        Similar_search_output = ", ".join(Similar_search)
                        st.write(Similar_search_output)
                    except:
                        st.info("something went wrong...")
                    

                    

    if __name__=="__main__":
        Wikisearch()


if Menu == "App info":
    def info_section():
        def info_html(html_file):
            with open(html_file) as f:
                st.markdown(f"{f.read()}",unsafe_allow_html=True)
    
        info_html("info.html")

    if __name__=="__main__":
        info_section()