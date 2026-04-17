# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tide.oli <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/04/14 13:05:38 by tide.oli          #+#    #+#              #
#    Updated: 2026/04/14 13:05:38 by tide.oli         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_recursive():
	harvest = int(input("Days until harvest: "))
	def recursive(harvest):
		if harvest > 1:
			recursive(harvest - 1)
		print(f"Day {harvest}")
	recursive(harvest)