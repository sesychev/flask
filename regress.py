import os
import pandas as pd
import ifcopenshell
from pathlib import Path
from time import gmtime, strftime
from tabulate import tabulate


def reg():
    source_dir = r"\\gle.local\all\home\e.sadovnikova\PUBLIC\IFC\ifc"
    # source_dir = r"\\gle-prj.gle.local\Prj\47.05-GSP.008\06_3D\01_Shared\Tekla"
    path_to_dir = Path(source_dir)
    print(path_to_dir)

    p = ['212']
    pc = ['214']
    c = ['201']
    b = ['204']
    secondary = ['13', '23']
    primary = [str(item) for item in range(4, 13)]
    primary.extend(['14', '26', '37', '2'])
    # print(primary)

    df = pd.DataFrame()
    open(os.path.join(path_to_dir, "regress.csv"), "w").close()
    open(os.path.join(path_to_dir, "errors.csv"), "w").close()

    for file in os.listdir(path_to_dir):
        filename = os.fsdecode(file)

        if filename.endswith(".ifc") and filename != 'G0-A10090RX0.ifc':
            path = os.path.join(path_to_dir, filename)
            ifc_file = ifcopenshell.open(path)
            file_dict = {}
            temp_df = pd.DataFrame()  # frame for .ifc file

            for product in ifc_file.by_type('IfcProduct'):
                psets = ifcopenshell.util.element.get_psets(product)
                temp_psets = psets.get('GLE_TeklaStructures', "HET")
                if temp_psets != "HET":
                    file_dict[filename] = temp_psets
                    a = pd.DataFrame(file_dict)
                    a = a.transpose()
                    temp_df = pd.concat([temp_df, a])
            try:
                piles = temp_df[temp_df['Class'].isin(p)]
                pilecaps = temp_df[temp_df['Class'].isin(pc)]
                columns = temp_df[temp_df['Class'].isin(c)]
                beams = temp_df[temp_df['Class'].isin(b)]

                '''
                print(
                    f"{filename}: Сваи:\t{len(piles)}\tшт.\t{(piles['Dry Weight'].sum() / 1000):.2f}\tт.")
                print(
                    f"{filename}: Ростверки:\t{len(pilecaps)}\tшт.\t{(pilecaps['Dry Weight'].sum() / 1000):.2f}\tт.")
                print(
                    f"{filename}: Колонны:\t{len(columns)}\tшт.\t{(columns['Dry Weight'].sum() / 1000):.2f}\tт.")
                print(
                    f"{filename}: Балки:\t{len(beams)}\tшт.\t{(beams['Dry Weight'].sum() / 1000):.2f}\tт.")
                '''

                primary1 = temp_df[temp_df['Class'].isin(primary) & (
                    temp_df['Dry Weight'] >= 10) & (temp_df['Dry Weight'] < 100)]
                primary2 = temp_df[temp_df['Class'].isin(primary) & (
                    temp_df['Dry Weight'] >= 100) & (temp_df['Dry Weight'] < 500)]
                primary3 = temp_df[temp_df['Class'].isin(primary) & (
                    temp_df['Dry Weight'] >= 500) & (temp_df['Dry Weight'] < 1000)]
                primary4 = temp_df[temp_df['Class'].isin(primary) & (
                    temp_df['Dry Weight'] >= 1000) & (temp_df['Dry Weight'] < 2000)]
                primary5 = temp_df[temp_df['Class'].isin(
                    primary) & (temp_df['Dry Weight'] >= 2000)]

                '''
               print(
                    f"{filename}: Основные стальные конструкции (10-100):\t{len(primary1)}\tшт.\t{(primary1['Dry Weight'].sum() / 1000):.2f}\tт.")
                print(
                    f"{filename}: Основные стальные конструкции (100-500):\t{len(primary2)}\tшт.\t{(primary2['Dry Weight'].sum() / 1000):.2f}\tт.")
                print(
                    f"{filename}: Основные стальные конструкции (500-1000):\t{len(primary3)}\tшт.\t{(primary3['Dry Weight'].sum() / 1000):.2f}\tт.")
                print(
                    f"{filename}: Основные стальные конструкции (1000-2000):\t{len(primary4)}\tшт.\t{(primary4['Dry Weight'].sum() / 1000):.2f}\tт.")
                print(
                    f"{filename}: Основные стальные конструкции (>2000):\t{len(primary5)}\tшт.\t{(primary5['Dry Weight'].sum() / 1000):.2f}\tт.")
                '''

                secondary1 = temp_df[temp_df['Class'].isin(
                    secondary) & (temp_df['Dry Weight'] < 10)]
                secondary2 = temp_df[temp_df['Class'].isin(
                    secondary) & (temp_df['Dry Weight'] >= 10)]

                '''
                print(
                    f"{filename}: Второстепенные стальные конструкции (<10):\t{len(secondary1)}\tшт.\t{(secondary1['Dry Weight'].sum() / 1000):.2f}\tт.")
                print(
                    f"{filename}: Второстепенные стальные конструкции (>10):\t{len(secondary2)}\tшт.\t{(secondary2['Dry Weight'].sum() / 1000):.2f}\tт.")

                print('=' * 3, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
                '''

                with open(os.path.join(path_to_dir, "regress.csv"), "a") as file:
                    # КЖ
                    file.write(
                        f"{filename}:\tСваи:\t{len(piles)}\tшт.\t{(piles['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                    file.write(
                        f"{filename}:\tРостверки:\t{len(pilecaps)}\tшт.\t{(pilecaps['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                    file.write(
                        f"{filename}:\tКолонны:\t{len(columns)}\tшт.\t{(columns['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                    file.write(
                        f"{filename}:\tБалки:\t{len(beams)}\tшт.\t{(beams['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                # КМ1
                    file.write(
                        f"{filename}:\tОсновные стальные конструкции (10-100):\t{len(primary1)}\tшт.\t{(primary1['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                    file.write(
                        f"{filename}:\tОсновные стальные конструкции (100-500):\t{len(primary2)}\tшт.\t{(primary2['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                    file.write(
                        f"{filename}:\tОсновные стальные конструкции (500-1000):\t{len(primary3)}\tшт.\t{(primary3['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                    file.write(
                        f"{filename}:\tОсновные стальные конструкции (1000-2000):\t{len(primary4)}\tшт.\t{(primary4['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                    file.write(
                        f"{filename}:\tОсновные стальные конструкции (>2000):\t{len(primary5)}\tшт.\t{(primary5['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                # КМ2
                    file.write(
                        f"{filename}:\tВторостепенные стальные конструкции (<10):\t{len(secondary1)}\tшт.\t{(secondary1['Dry Weight'].sum() / 1000):.2f}\tт.\n")
                    file.write(
                        f"{filename}:\tВторостепенные стальные конструкции (>10):\t{len(secondary2)}\tшт.\t{(secondary2['Dry Weight'].sum() / 1000):.2f}\tт.\n")
            except Exception as e:
                # print('ОШИБКИ:')
                print(f"{filename}: Тип ошибки: {e}")
                with open(os.path.join(path_to_dir, "errors.csv"), "a") as file:
                    file.write(f"{filename}:\tТип ошибки: {e}\n")

            df = pd.concat([df, temp_df])

    df.to_csv(os.path.join(
        path_to_dir, "df.csv"), sep='\t', encoding='utf-8')

    piles = df[df['Class'].isin(p)]
    pilecaps = df[df['Class'].isin(pc)]
    columns = df[df['Class'].isin(c)]
    beams = df[df['Class'].isin(b)]

    primary1 = df[df['Class'].isin(primary) & (
        df['Dry Weight'] >= 10) & (df['Dry Weight'] < 100)]
    primary2 = df[df['Class'].isin(primary) & (
        df['Dry Weight'] >= 100) & (df['Dry Weight'] < 500)]
    primary3 = df[df['Class'].isin(primary) & (
        df['Dry Weight'] >= 500) & (df['Dry Weight'] < 1000)]
    primary4 = df[df['Class'].isin(primary) & (
        df['Dry Weight'] >= 1000) & (df['Dry Weight'] < 2000)]
    primary5 = df[df['Class'].isin(primary) & (
        df['Dry Weight'] >= 2000)]

    secondary1 = df[df['Class'].isin(
        secondary) & (df['Dry Weight'] < 10)]
    secondary2 = df[df['Class'].isin(
        secondary) & (df['Dry Weight'] >= 10)]

    print(tabulate([["Сваи", f"{p}", f'{len(piles)}', f"{(piles['Dry Weight'].sum() / 1000):.2f}"], ['Ростверки', f"{pc}", f'{len(pilecaps)}', f"{(pilecaps['Dry Weight'].sum() / 1000):.2f}"], ['Колонны', f"{c}", f'{len(columns)}', f"{(columns['Dry Weight'].sum() / 1000):.2f}"], ['Балки', f"{b}", f'{len(beams)}', f"{(beams['Dry Weight'].sum() / 1000):.2f}"], ['Основные стальные конструкции (10-100)', f"{primary}", f"{len(primary1.index)}", f"{(primary1['Dry Weight'].sum() / 1000):.2f}"], [
        'Основные стальные конструкции (100-500)', f"{primary}", f"{len(primary2)}", f"{(primary2['Dry Weight'].sum() / 1000):.2f}"], ['Основные стальные конструкции (500-1000))', f"{primary}", f"{len(primary3)}", f"{(primary3['Dry Weight'].sum() / 1000):.2f}"], ['Основные стальные конструкции (1000-2000)', f"{[item for item in primary]}", f"{len(primary4)}", f"{(primary4['Dry Weight'].sum() / 1000):.2f}"], ['Основные стальные конструкции (>2000)', f"{primary}", f"{len(primary5)}", f"{(primary5['Dry Weight'].sum() / 1000):.2f}"], ['Второстепенные стальные конструкции (<10)', f"{secondary}", f"{len(secondary1.index)}", f"{(secondary1['Dry Weight'].sum() / 1000):.2f}"], ['Второстепенные стальные конструкции (>10)', f"{secondary}", f"{len(secondary2.index)}", f"{(secondary2['Dry Weight'].sum() / 1000):.2f}"]], headers=['Описание', 'Class', 'Кол-во, шт', 'Dry Weight, т'], tablefmt='orgtbl'))

    txt = f"Сваи (212):\t{len(piles)}\tшт.\t{(piles['Dry Weight'].sum() / 1000):.2f}\tт.\nРостверки (214):\t{len(pilecaps)}\tшт.\t{(pilecaps['Dry Weight'].sum() / 1000):.2f}\tт.\nКолонны (201):\t{len(columns)}\tшт.\t{(columns['Dry Weight'].sum() / 1000):.2f}\tт.\nБалки (204):\t{len(beams)}\tшт.\t{(beams['Dry Weight'].sum() / 1000):.2f}\tт.\nОсновные ('2','4','5','6','7','8','9','10','11','12','14','26','37') стальные конструкции (10-100):\t{len(primary1)}\tшт.\t{(primary1['Dry Weight'].sum() / 1000):.2f}\tт.\nОсновные ('2','4','5','6','7','8','9','10','11','12','14','26','37') стальные конструкции (100-500):\t{len(primary2)}\tшт.\t{(primary2['Dry Weight'].sum() / 1000):.2f}\tт.\nОсновные ('2','4','5','6','7','8','9','10','11','12','14','26','37') стальные конструкции (500-1000):\t{len(primary3)}\tшт.\t{(primary3['Dry Weight'].sum() / 1000):.2f}\tт.\nОсновные ('2','4','5','6','7','8','9','10','11','12','14','26','37') стальные конструкции (1000-2000):\t{len(primary4)}\tшт.\t{(primary4['Dry Weight'].sum() / 1000):.2f}\tт.\nОсновные ('2','4','5','6','7','8','9','10','11','12','14','26','37') стальные конструкции (>2000):\t{len(primary5)}\tшт.\t{(primary5['Dry Weight'].sum() / 1000):.2f}\tт.\nВторостепенные (13,23) стальные конструкции (<10):\t{len(secondary1)}\tшт.\t{(secondary1['Dry Weight'].sum() / 1000):.2f}\tт.\nВторостепенные (13,23) стальные конструкции (>10):\t{len(secondary2)}\tшт.\t{(secondary2['Dry Weight'].sum() / 1000):.2f}\tт."
    return txt
