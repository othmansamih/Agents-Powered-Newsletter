from newsletter_gen.crew import NewsletterGen
import streamlit as st

class NewsletterGenUI:
    def load_html_template(self):
        with open("src/newsletter_gen/config/newsletter_template.html", "r") as file:
            html_template = file.read()
        return html_template
    
    def load_newsletter(self):
        with open("tasks/newsletter_task.html", "r") as file:
            html_template = file.read()
        return html_template

    def generate_newsletter(self, topic, personal_message):
        inputs = {
            'topic': topic,
            'personal_message': personal_message,
            'html_template': self.load_html_template()
        }
        return NewsletterGen().crew().kickoff(inputs=inputs)
    
    def newsletter_generation(self):
        if st.session_state.generating:
            st.session_state.newsletter = self.generate_newsletter(
                st.session_state.topic,
                st.session_state.personal_message
            )

            if str(st.session_state.newsletter):
                st.write("The newsletter has been generated successfully!")
                st.html(self.load_newsletter())

                st.download_button(
                    label="Download Newsletter",
                    data=str(st.session_state.newsletter),
                    file_name=f"{st.session_state.topic} Newsletter.html",
                    mime="text/html"
                )

                st.session_state.generating = False


    def sidebar(self):
        with st.sidebar:
            st.title("Newsletter Generator")
            st.text_input(
                label="Enter the topic of the newsletter",
                key="topic",
                placeholder="Latest news about AI"
            )
            st.text_area(
                label="Enter the personal message of the newsletter",
                key="personal_message",
                placeholder="The Osamih newsletter"
            )

            if st.button("Generate the newsletter"):
                st.session_state.generating = True


    def render(self):
        st.set_page_config(
            page_title="Your ultimate newsletter",
            page_icon=" 📰",
            layout="centered"
        )
        
        if "topic" not in st.session_state:
            st.session_state.topic = ""
        
        if "personal_message" not in st.session_state:
            st.session_state.personal_message = ""
        
        if "generating" not in st.session_state:
            st.session_state.generating = False
        
        if "generated_newsletter" not in st.session_state:
            st.session_state.newsletter = ""
        
        self.sidebar()

        self.newsletter_generation()




if __name__ == "__main__":
    NewsletterGenUI().render()
