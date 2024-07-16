import streamlit as st
def c_w(w,c):
    g=9.81
    g_moon = 1.625
    g_jupiter = 24.79
    g_mars = 3.71
    g_mercury = 3.7
    g_neptune = 11.55
    g_pluto = 0.62
    g_saturn = 10.44
    g_uranus = 8.87
    g_venus = 8.87
    g_sun = 274
    if w>0:
        if c=='Earth':
            return w
        elif c=='Moon':
            return w*g_moon/g
        elif c=='Jupiter':
            return w*g_jupiter/g
        elif c=='Mars':
            return w*g_mars/g
        elif c=='Mercury':
            return w*g_mercury/g
        elif c=='Neptune':
            return w*g_neptune/g
        elif c=='Pluto':
            return w*g_pluto/g
        elif c=='Saturn':
            return w*g_saturn/g
        elif c=='Uranus':
            return w*g_uranus/g
        elif c=='Venus':
            return w*g_venus/g
        elif c=='Sun':
            return w*g_sun/g
    else:
        return None
def main():
    st.title("Calculate weight on planets.")
    st.text("-By Saurav Chaudhari")
    w = st.number_input("Enter your weight in kg : ",min_value=0.0)
    Planet = ['','Earth','Moon','Jupiter','Mars','Mercury','Neptune','Pluto','Saturn','Uranus','Venus','Sun']
    p_n=st.selectbox("Enter the name of planet : ",Planet)
    if st.button("Calculate"):
        if w > 0:
            cd_w=c_w(w,p_n)
            if cd_w is not None:
                st.write(f'Your weight on {p_n} is {round(cd_w,2)} kg.')
            else:
                st.write('Invalid planet selection.')
        else:
            st.write('Please enter a valid weight.')



if __name__ == '__main__':
    main()


