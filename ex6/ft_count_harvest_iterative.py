# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tide.oli <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/14 13:05:17 by tide.oli          #+#    #+#              #
#    Updated: 2026/04/14 13:05:17 by tide.oli         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	harvest = int(input("Days until harvest: "))
	for i in range (1, (harvest + 1)):
		print(f"Day {i}")