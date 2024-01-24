import flet as ft

def show_selected_dir(e: ft.FilePickerResultEvent):
    print(e.path)



def main(page : ft.Page):
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    page.update()

    btn = ft.ElevatedButton('Choose an image...',on_click=lambda _: file_picker.get_directory_path())
    page.add(btn)
    

ft.app(target=main)