import random


def draw_card():
    """Генерирует случайную карту (число от 2 до 11)."""
    return random.randint(2, 11)


def game():
    # Начальные карты игроков
    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card()]

    print(f"Ваши карты: {player_cards}, ваша сумма: {sum(player_cards)}")
    print(f"Карта дилера: {dealer_cards}")

    while True:
        action = input("Хотите взять карту ('y') или остановиться ('n')? ").strip().lower()

        if action == 'y':
            new_card = draw_card()
            player_cards.append(new_card)
            print(f"Получили карту: {new_card}. Ваша новая сумма: {sum(player_cards)}.")

            if sum(player_cards) > 21:
                print("Перебор! Вы проиграли.")
                break
        elif action == 'n':
            break
        else:
            print("Неправильный ввод. Попробуйте снова.")

    # Теперь ход дилера
    while sum(dealer_cards) < 17:
        new_dealer_card = draw_card()
        dealer_cards.append(new_dealer_card)
        print(f"Дилер получил карту: {new_dealer_card}. Его сумма: {sum(dealer_cards)}.")

    # Итоги игры
    player_total = sum(player_cards)
    dealer_total = sum(dealer_cards)

    print("\nИтоговая ситуация:")
    print(f"Ваша итоговая сумма: {player_total}")
    print(f"Сумма дилера: {dealer_total}")

    if player_total <= 21 and (dealer_total > 21 or player_total > dealer_total):
        print("Поздравляем! Вы выиграли!")
    elif player_total == dealer_total:
        print("Ничья!")
    else:
        print("К сожалению, вы проиграли.")


if __name__ == "__main__":
    game()