# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tide.oli <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/14 11:35:47 by tide.oli          #+#    #+#              #
#    Updated: 2026/04/14 11:35:47 by tide.oli         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

units = ["packets", "grams", "area"]
unit_format = [" avaiable", " total", ""]
def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit not in units:
		print("Unknown unit type")
		return
	print((f"{seed_type.capitalize()} seeds: {quantity} {unit}{
				unit_format[units.index(unit)]}."))
