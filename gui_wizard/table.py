from cvs import *
class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        wid = gui.VBox(width=500, height=500, style={'margin':'5px auto', 'padding': '10px'})

        lbl_description = gui.Label("""Example about TableWidget usage.
                                    Change rows and columns count in order to see the behaviour. 
                                    After changing the size, 'Fill the table' content by means of the button.""")

        wid.append(lbl_description)

        table = gui.TableWidget(10, 3, True, True, width=300, height=300)
        table.style['font-size'] = '8px'

        container = gui.HBox(width='100%')
        lbl_row_count = gui.Label('Rows:')
        spin_row_count = gui.SpinBox(10, 0, 15)
        spin_row_count.onchange.do(self.on_row_count_change, table)
        container.append(lbl_row_count)
        container.append(spin_row_count)
        wid.append(container)

        container = gui.HBox(width='100%')
        lbl_column_count = gui.Label('Columns:')
        spin_column_count = gui.SpinBox(3, 0, 4)
        spin_column_count.onchange.do(self.on_column_count_change, table)
        container.append(lbl_column_count)
        container.append(spin_column_count)
        wid.append(container)

        bt_fill_table = gui.Button('Fill table', width=100)
        bt_fill_table.onclick.do(self.fill_table, table)
        wid.append(bt_fill_table)

        chk_use_title = gui.CheckBoxLabel('Use title', True)
        chk_use_title.onchange.do(self.on_use_title_change, table)
        wid.append(chk_use_title)

        self.fill_table(table, table)

        table.on_item_changed.do(self.on_table_item_changed)

        wid.append(table)
        # returning the root widget
        return wid

    def on_row_count_change(self, emitter, value, table):
        table.set_row_count(int(value))

    def on_column_count_change(self, emitter, value, table):
        table.set_column_count(int(value))

    def fill_table(self, emitter, table):
        for ri in range(0, table.row_count()):
            for ci in range(0, table.column_count()):
                table.item_at(ri, ci).set_text("row:%s,column:%s"%(str(ri),str(ci)))

    def on_use_title_change(self, emitter, value, table):
        value = value == 'true'
        table.set_use_title(value)

    def on_table_item_changed(self, table, item, new_value, row, column):
        print("text: %s    row: %s    column: %s"%(new_value, row, column))


if __name__ == "__main__":
    initcv(cvs.openwin)
    startcv(MyApp)

