import pandas as pd
import pydeck as pdk
import streamlit as st

import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.pset
# from ifc_viewer import ifc_viewer

ifc_file = ifcopenshell.open('static/ifc/____P0-02-070.ifc')

def from_ifc():
    return pd.DataFrame(ifc_file.types())

session = st.session_state

products = ifc_file.by_type('IfcProduct')
keys = []
wap = {}
output = pd.DataFrame()
get = pd.DataFrame()

for product in products:
    psets = ifcopenshell.util.element.get_psets(product)
    for k, v in psets.items():
        if k not in keys:
            keys.append(k)

                # if product.Name == 'Связь горизонтальная':
            temp = psets.get('GLE_TeklaStructures', "HET")
                # x = json.dumps(temp)
            # print(json.loads(x))
            # print(temp)
            t = {}
            if temp != "HET":
                    # t['CWA']=t['CWA']
                    # wap['CWA'] = temp['CWA']
                    # t['Phase'] = temp['Phase']
                    # t['Class'] = temp['Class']
                    # t['ProfileWeightPerUnitLength'] = temp['ProfileWeightPerUnitLength']
                    # print(f"{product.is_a()}, CWA={temp['CWA']} Phase={temp['Phase']} Class={temp['Class']} ProfileWeightPerUnitLength={temp['ProfileWeightPerUnitLength']}")
                wap[ifc_file.by_type("IfcProject")[0].get_info()[
                        'Name']] = temp
            # print(temp)
                a = pd.DataFrame(wap)
                a = a.transpose()
                output = pd.concat([output, a])

            # print(psets.get('GLE_TeklaStructures'))
            # output = output.append(wap, ignore_index=True)
            # print(wap)
output
            # print(temp)

def execute():
    tab1, tab2 = st.tabs(["review", "quantities"])
      
    with tab1:
        st.header("Review")
        session["ifc"] = output
        st.write(session["ifc"])
    with tab1:
        st.header("Quantities")
        
        area = st.selectbox("Column", options = output.columns)
        session['sdsd'] = output[area]
        st.write(session['sdsd'])
        st.write("Общее количество: ", sum(output["Area PX"]))
        st.write("Общее количество: ", len(session['sdsd']))
        
        
        
        plan = st.selectbox("Area Plan", output['Area Plan'].unique())
        #p = st.multiselect("Profile Standard Name", output['Profile Standard Name'].unique())
        #n = output[(output["Section Name"].isin(q)) & (output["Profile Standard Name"].isin(p))]
        c = st.multiselect("Class", output['Class'].unique())
        
        m = output[output["Class"].isin(c)]
        st.write(m)
        st.write("Общее количество: ", len(m))
execute()
