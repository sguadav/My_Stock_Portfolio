import get_data
import current_command
import edit_command


def home_input():
    continue_program = True
    print("\nHello Santiago,")
    while continue_program:
        print("\nThis is your Virtual Stock Portfolio (VSP), where you can manage your stocks.\n"
              "You can:\n"
              "a) 'Current': See My Portfolio and current earnings.\n"
              "b) 'Edit': Change My Portfolio or Add a new stock.\n"
              "c) 'Explore': Check out and analyze a new stock.\n"
              "d) 'Exit': Stop the program.\n")
        intro_command_input = input("Enter the command: ")
        if intro_command_input == 'Current':
            myPortfolio = get_data.open_portfolio()  # IDK WHY DOESN'T WORK
            print("\nmyPortfolio:")
            print(myPortfolio)
            earnings_percentage_list, earnings_dollars_list = current_command.current_earnings(myPortfolio)
            current_command.print_earnings(myPortfolio, earnings_percentage_list, earnings_dollars_list)
            in_depth_command = input("\nDo you want to take a look at a specific stock? Yes or No? ")
            current_continue = False if ((in_depth_command == 'No') or (in_depth_command == 'no')) else True
            while current_continue:
                stock_evaluating = input("From MyPortfolio, Which stock do you want to take a look at? ")

                print("\nWith the stocks of My Portfolio, you can:\n"
                      "a) 'Graphs': Get the current graph for the stock and the analytics graph\n"
                      "b) 'Intrinsic': Calculate the intrinsic value\n"
                      "c) 'Back': Go back\n")
                current_command_input = input("Enter the command: ")
                if current_command_input == 'Graphs':
                    stock_data = get_data.get_stock_data(stock_evaluating)  # Can put it as a variable in the menu to avoid this step over and over
                    current_command.stock_graph(stock_evaluating, stock_data)
                    current_command.stock_graph_MACD(stock_evaluating, stock_data)
                elif current_command_input == 'Intrinsic':
                    stock_intrinsic_val, stock_upside, current_value = current_command. \
                        intrinsic_val_calculation(stock_evaluating)
                    print("\nIntrinsic Value Calculation:")
                    print("Stock:", stock_evaluating)
                    print("Current Value : $ {:.2f}".format(current_value))
                    print("Intrinsic Value: $ {:.2f}".format(stock_intrinsic_val))
                    print("Upside : % {:.2f}\n".format(stock_upside))
                elif current_command_input == 'Back':
                    break
                else:
                    print("Please type the command correctly")
                current_repeat = input("Do you want to check something else in 'Current'? 'Yes' or 'No': ")
                current_continue = False if ((current_repeat == 'No') or (current_repeat == 'no')) else True

        elif intro_command_input == 'Edit':
            edit_continue = True
            while edit_continue:
                print("For this section you can:\n"
                      "a) 'Add': Add a new stock to your portfolio\n"
                      "b) 'Delete': Delete a stock\n"
                      "c) 'Back': Go back\n")
                edit_command_input = input("Enter the command: ")
                if edit_command_input == 'Add':
                    edit_command.add_to_csv()
                elif edit_command_input == 'Delete':
                    edit_command.delete_csv_row()
                elif edit_command_input == 'Back':
                    break
                else:
                    print("Please type the command correctly")
                edit_repeat = input("Do you want to check something else in 'Edit'? Yes or No: ")
                edit_continue = False if ((edit_repeat == 'No') or (edit_repeat == 'no')) else True

        elif intro_command_input == 'Explore':
            explore_continue = True
            while explore_continue:
                exploring_stock = input("What stock ticker symbol you want to take a look at? ")
                print("\nFor '", exploring_stock, "' you can:\n"
                                                  "a) 'Graphs': Get the current graph for the stock and the analytics "
                                                  "graph\n"
                                                  "b) 'Intrinsic': Calculate the intrinsic value\n"
                                                  "c) 'Back': Go back\n")
                explore_command_input = input("Enter the command: ")
                if explore_command_input == 'Graphs':
                    explore_stock_data = get_data.get_stock_data(exploring_stock)
                    current_command.stock_graph(exploring_stock, explore_stock_data)
                    current_command.stock_graph_MACD(exploring_stock, explore_stock_data)
                elif explore_command_input == 'Intrinsic':
                    explore_stock_intrinsic_val, explore_stock_upside, explore_current_value = current_command. \
                        intrinsic_val_calculation(exploring_stock)
                    print("\nIntrinsic Value Calculation:")
                    print("Stock:", exploring_stock)
                    print("Current Value : $ {:.2f}".format(explore_current_value))
                    print("Intrinsic Value: $ {:.2f}".format(explore_stock_intrinsic_val))
                    print("Upside : % {:.2f}\n".format(explore_stock_upside))
                elif explore_command_input == 'Back':
                    break
                else:
                    print("Please type the command correctly")
                explore_repeat = input("Do you want to check something else in 'Explore'? 'Yes' or 'No'? ")
                explore_continue = False if ((explore_repeat == 'No') or (explore_repeat == 'no')) else True

        elif intro_command_input == 'Exit':
            break

        else:
            print("Please type the command correctly")

        is_repeat = input("Do you want to check something else in the General Menu? 'Yes' or 'No'? ")
        continue_program = False if ((is_repeat == 'No') or (is_repeat == 'no')) else True


if __name__ == '__main__':
    home_input()
