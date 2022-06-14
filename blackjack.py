from random import randint

def card_deck():
    #sets the card types and values

    card_value = ['A', '2', '3', '4', '5', '6', '7','8', '9', '10', 'J', 'Q', 'K']
    card_type = ['Coração', 'Espadas', 'Copas', 'Ouros'] # Coração, Espadas, Copas, Ouros
    deck = []

    #This iterates all 52 cards into a deck

    for i in card_type:
        for j in card_value:
            deck.append(j + ' de ' + i)
    return deck

def card_value(card):
    #only reading first slide to determine value of the card

    if card[:1] in ('J', 'Q', 'K', '1'):
        return int(10)
    
    elif card[:1] in ('2', '3', '4', '5', '6', '7', '8', '9'):
        #card[:1] example '2' out of the full '2 of Hearts' string

        return int(card[:1])

    elif card[:1] == 'A':
        print("\n" + str(card))
        num = input("Você quer que isso seja 1 ou 11?\n> ")

        while num != '1' or num != '11':
            if num == '1':
                return int(1)

            elif num == '11':
                return int(11)

            else:
                num = input("Você quer que isso seja 1 ou 11?\n> ")


def new_card(deck):
    return deck[randint(0,len(deck)-1)]

def remove_card(deck, card):
    return deck.remove(card)


play_again = ''

while play_again != 'SAIR':
    #deck creation, card creation, card removal from deck, values and totals

    new_deck = card_deck()
    card1 = new_card(new_deck)
    remove_card(new_deck,card1)
    card2 = new_card(new_deck)
    remove_card(new_deck, card2)

    print("\n\n\n\n" + card1 + " e " + card2) #doing this statement first allows for selection between 1 and 11

    valu1 = card_value(card1)
    valu2 = card_value(card2)
    total = valu1 + valu2
    print("Com um total de " + str(total))

    #dealer's hand

    dealer_card1 = new_card(new_deck)
    remove_card(new_deck, dealer_card1)
    dealer_card2 = new_card(new_deck)
    remove_card(new_deck, dealer_card2)
    dealer_value1 = card_value(dealer_card1)
    dealer_value2 = card_value(dealer_card2)
    dealer_total = dealer_value1 + dealer_value2

    print('\nO Dealer sorri enquanto olha para você e\ndistribui uma carta para cima e uma carta virada para baixo\n')
    print("Primeiro um " + dealer_card1 + " e carta virada para baixo.")

    if total == 21:
        print("BLACKJACK!")

    else:
        while total < 21: #not win or loss yet
            answer = input("Você quer Pegar ou Manter?\n> ")
        
            if answer.lower() == 'pegar':
                #more card creation, removal, and value added to total
                more_card = new_card(new_deck)
                remove_card(new_deck, more_card)
                more_value = card_value(more_card)
                total += int(more_value)

                print(more_card + " um novo total de " + str(total))

                if total > 21: #lose condition
                    print("VOCÊ PERDEU!")
                    play_again = input("Gostaria de continuar? SAIR para sair\n")

                elif total == 21: #winning condition
                    print("VOCÊ VENCEU!!!")
                    play_again = input("Gostaria de continuar? SAIR para sair\n")

                else:
                    continue

            elif answer.lower() == 'manter':
                print("O dealer acena com a cabeça e revela que sua outra carta é ")
                print("um " + dealer_card2 + " de um novo total de " + str(dealer_total))

                if dealer_total < 17:
                    print("O Dealer bate novamente.")
                    dealer_more = new_card(new_deck)
                    more_dealer_value = card_value(dealer_more)
                    print("A carta é um " + str(dealer_more))
                    dealer_total += int(more_dealer_value)

                    if dealer_total > 21 and total <= 21:
                        print("O Dealer perdeu! Você Venceu!")

                    elif dealer_total < 21 and dealer_total > total:
                        print("O Dealer tem" + str(dealer_total) + " Você Perdeu!")

                    else:
                        continue

                elif dealer_total == total:
                    print("Empate, sem vencendor")
                elif dealer_total < total:
                    print("Você Venceu!")
                else:
                    print("Você Perdeu!")

                play_again = input("\Gostaria de continuar? SAIR para sair\n> ")
                break

int("Obrigado por jogar, volte sempre!")
