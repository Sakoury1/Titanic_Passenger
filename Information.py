import streamlit as st

with st.sidebar :
    st.markdown(
     """
        <div style="display: flex; gap: 20px; align-items: center;">
         <a href="https://www.linkedin.com/in/zyad-sakoury-135405261/" target="_blank">
              <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="40"/>
            </a>
            <a href="https://www.facebook.com/zyad.ahmedsakoury" target="_blank">
             <img src="https://cdn-icons-png.flaticon.com/512/733/733547.png" alt="Facebook" width="40"/>
         </a>
        </div>
        """,
        unsafe_allow_html=True
    )
st.title("Titanic Information 🚢")


st.image("Stöwer_Titanic.jpg",width=800)
st.info("The Titanic: A Tragic Story The RMS Titanic was a British passenger liner that tragically sank on its maiden voyage. It was one of the largest and most luxurious ships of its time, built by the White Star Line. The Titanic set sail from Southampton, England, on April 10, 1912, heading for New York City. On the night of April 14, 1912, the ship struck an iceberg in the North Atlantic Ocean. The collision caused severe damage, and within a few hours, the Titanic broke apart and sank in the early hours of April 15. Out of approximately 2,224 passengers and crew on board, more than 1,500 lost their lives due to the freezing waters and a shortage of lifeboats. The Titanic was considered unsinkable due to its advanced design and watertight compartments. However, the disaster revealed flaws in safety regulations, leading to significant improvements in maritime safety, including stricter lifeboat requirements and better emergency procedures. The wreck of the Titanic was discovered in 1985, lying at a depth of about 12,500 feet (3,800 meters) in the Atlantic Ocean. Today, the story of the Titanic remains one of the most famous maritime tragedies in history, inspiring books, documentaries, and movies. ")