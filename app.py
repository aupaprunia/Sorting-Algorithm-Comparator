import random
import time

import flet as ft

from heap_sort import heapsort
from bubble_sort import bubblesort
from insertion_sort import insertion
from regular_quick_sort import quick_sort_main
from merge_sort import mergesort
from selection_sort import selection
from three_median_quick_sort import quick_sort_3_median_main


def app(page : ft.Page):
    sorting_algo_map = {"Quick Sort with 3-medians": quick_sort_3_median_main, 
                            "Bubble Sort": bubblesort, "Heap Sort": heapsort,
                            "Insertion Sort": insertion, "Merge Sort": mergesort,
                            "Regular Quick Sort": quick_sort_main, "Selection Sort": selection}
    
    sorting_algo_time_complexity = {"Quick Sort with 3-medians": "n*log(n)", 
                            "Bubble Sort": "n^2", "Heap Sort": "n*log(n)",
                            "Insertion Sort": "n^2", "Merge Sort": "n*log(n)",
                            "Regular Quick Sort": "n^2", "Selection Sort": "n^2"}

    # For choosing algorithm
    def next_action_1(e):
        if algo_dropdown.value:
            algo_dropdown.error_text = None
            input_type_text.visible = True
            input_dropdown.visible = True
    
        else:
            algo_dropdown.error_text = "Please select an algorithm"
        
        no_to_generate_text.visible = False
        txt_number.visible = False
        plus_minus_icons.visible = False
        done_btn.visible = False

        input_text_box.visible = False
        input_text_box_prompt.visible = False
        done_btn_2.visible = False

        input_array_txt.visible = False
        input_array_txt.value = None
        sort_btn.visible = False

        page.update()

    # For choosing input type
    def next_action_2(e):
        if input_dropdown.value:
            input_dropdown.error_text = None
            if input_dropdown.value == "Randomly generated (between -1000 and 1000)":
                no_to_generate_text.visible = True
                txt_number.visible = True
                plus_minus_icons.visible = True
                done_btn.visible = True

                input_text_box.visible = False
                input_text_box_prompt.visible = False
                done_btn_2.visible = False

            else:
                no_to_generate_text.visible = False
                txt_number.visible = False
                plus_minus_icons.visible = False
                done_btn.visible = False

                input_text_box.visible = True
                input_text_box_prompt.visible = True
                done_btn_2.visible = True

        else:
            input_dropdown.error_text = "Please select an input type"
        
        input_array_txt.visible = False
        input_array_txt.value = None
        sort_btn.visible = False

        page.update()
    
    # On minus click
    def minus_click(e):
        if int(txt_number.value) > 1:
            txt_number.value = str(int(txt_number.value) - 1)
            page.update()

    # On plus click
    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    
    # For choosing numbers to generate
    def done_btn_action_1(e):
        numbers_to_generate = int(txt_number.value) 
        if numbers_to_generate > 0:
            txt_number.error_text = None
            if numbers_to_generate > 2000:
                numbers_to_generate = 2000
            global input_arr
            input_arr = list(random.sample(range(-1000, 1000), numbers_to_generate))
            input_array_txt.visible = True
            input_array_txt.value = f"\nThe array to be sorted is -> {input_arr}"
            sort_btn.visible = True
        
        else:
            txt_number.error_text = "Invalid value"
        
        page.update()
    
    # Helper function
    def convert_to_list(strs):
        str_list = strs.split(",")
        input_arr = []
        for c in str_list:
            try:
                input_arr.append(int(c))
            except:
                pass
        
        return input_arr

    # For user input
    def done_btn_action_2(e):
        if input_text_box.value != "":
            global input_arr
            input_arr = convert_to_list(input_text_box.value)
            input_text_box.error_text = None
            input_array_txt.visible = True
            input_array_txt.value = f"\nThe array to be sorted is -> {input_arr}"
            sort_btn.visible = True
        else:
            input_text_box.error_text = "Please enter some values"
        
        page.update()
    
    # Sort array button
    def sort_btn_action(e):
        algo_name = algo_dropdown.value
        start_time1 = time.perf_counter()
        expected_arr = sorting_algo_map[algo_name](input_arr)
        end_time1 = time.perf_counter()
        expected_exec_time = (end_time1 - start_time1) * 100000
        chart_colours = [ft.colors.PURPLE, ft.colors.AMBER, ft.colors.BLUE, ft.colors.RED, ft.colors.ORANGE, ft.colors.GREEN, ft.colors.BLACK]
        rows = []
        bar_groups = [ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=expected_exec_time,
                        width=40,
                        color=chart_colours[0],
                        tooltip=algo_name,
                        border_radius=0,
                    ),
                ],
            )]
        labels = [ft.ChartAxisLabel(
                    value=0, label=ft.Container(ft.Text(algo_name), padding=10)
                )]
        x = 0
        for k,v in sorting_algo_map.items():
            if k != algo_name:

                start_time = time.perf_counter()
                v(input_arr)
                end_time = time.perf_counter()
                exec_time = (end_time - start_time) * 100000
                rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(f"{k}")),
                            ft.DataCell(ft.Text(f"{sorting_algo_time_complexity[k]}")),
                            ft.DataCell(ft.Text(f"{exec_time:.4f} x 10^-5"))]))
                bar_groups.append(ft.BarChartGroup(
                x=x,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=exec_time,
                        width=40,
                        color=chart_colours[x+1],
                        tooltip=k,
                        border_radius=0,
                    ),
                ],
            ))
                labels.append(ft.ChartAxisLabel(
                    value=x+1, label=ft.Container(ft.Text(k), padding=10)
                ))
                x += 1

        comparision_table.rows = rows
        page.views.clear()
        sorted_array.visible = True
        sorted_array.value = f"The sorted array is {expected_arr}\nExecution Time: {expected_exec_time:.4f} x 10^-5 seconds"
        chart.bar_groups = bar_groups
        chart.bottom_axis = ft.ChartAxis(labels=labels, labels_size=1)
        page.views.append(new_view)
        page.update()

    def dark_mode_toggle(e):
        if dark_mode_icon.icon == ft.icons.DARK_MODE:
            dark_mode_icon.icon = ft.icons.LIGHT_MODE
            dark_mode_icon.icon_color = "white"
            page.theme_mode = ft.ThemeMode.DARK
        else:
            dark_mode_icon.icon = ft.icons.DARK_MODE
            dark_mode_icon.icon_color = "black"
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    page.title = "Sorting algorithms"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # Heading
    dark_mode_icon = ft.IconButton(
                    icon=ft.icons.DARK_MODE,
                    icon_color="black",
                    icon_size=20,
                    tooltip="Toggle",
                    on_click=dark_mode_toggle
                )
    dark_mode_container = ft.Container(dark_mode_icon, margin=ft.Margin(left=150, top=0, right=0, bottom=0))
    heading_container = ft.Container(ft.Text("SORTING ALGORITHMS", weight=ft.FontWeight.BOLD, size=30), margin=ft.Margin(left=200, top=0, right=0, bottom=0))
    
    page.add(ft.Row([heading_container, dark_mode_container], alignment=ft.MainAxisAlignment.CENTER))

    # Sorting algorithm dropdown
    page.add(ft.Text("Choose a sorting algorithm"))
    algo_dropdown = ft.Dropdown(
        width=500,
        hint_text="Select",
        options=[
            ft.dropdown.Option("Bubble Sort"),
            ft.dropdown.Option("Heap Sort"),
            ft.dropdown.Option("Insertion Sort"),
            ft.dropdown.Option("Merge Sort"),
            ft.dropdown.Option("Regular Quick Sort"),
            ft.dropdown.Option("Selection Sort"),
            ft.dropdown.Option("Quick Sort with 3-medians"),
        ],
        on_change=next_action_1
    )

    page.add(algo_dropdown)

    # Input type
    input_type_text = ft.Text("Choose input type", visible=False)

    input_dropdown = ft.Dropdown(
    width=500,
    hint_text="Select",
    options=[
        ft.dropdown.Option("Randomly generated (between -1000 and 1000)"),
        ft.dropdown.Option("I'll enter it myself!")
    ],
    visible=False,
    on_change=next_action_2
    )

    page.add(input_type_text)
    page.add(input_dropdown)

    # Numbers to generate
    no_to_generate_text = ft.Text("Enter numbers to generate", visible=False)

    txt_number = ft.TextField(value="1", text_align="center", width=100, visible=False)

    plus_minus_icons = ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            visible=False
        )

    done_btn = ft.TextButton(text="Next", on_click=done_btn_action_1,visible=False)

    page.add(no_to_generate_text)
    page.add(plus_minus_icons)
    page.add(done_btn)

    # Show input box
    input_text_box_prompt = ft.Text(value="Enter the number you want to sort sepearted by commas", visible=False)
    input_text_box = ft.TextField(visible=False, width=500)
    done_btn_2 = ft.TextButton(text="Done", on_click=done_btn_action_2, visible=False)
    
    page.add(input_text_box_prompt)
    page.add(input_text_box)
    page.add(done_btn_2)

    # Show array to be sorted
    input_array_txt = ft.Text(visible=False, size="15")
    page.add(input_array_txt)

    #Sort array button
    sort_btn = ft.TextButton(text="Sort Array", visible=False, on_click=sort_btn_action)
    page.add(sort_btn)

    # Show sorted array
    sorted_array = ft.Text(visible=False)

    comparision_table = ft.DataTable(
        columns=[ft.DataColumn(ft.Text("Algorithm Name")),
                ft.DataColumn(ft.Text("Worst case time complexity")),
                ft.DataColumn(ft.Text("Execution Time (in s)"))],
    )

    chart = ft.BarChart(border=ft.border.all(1, ft.colors.GREY_400),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Execution Time"), title_size=25
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
        max_y=15,
        interactive=True,
        expand=True)
    new_view = ft.View(route = '/', controls=[sorted_array, comparision_table, chart])
    
ft.app(target=app)