def fit_pair_to_list(pair_list, new_pair):
	new_pair_list = []
	for pair in pair_list:
		if new_pair and pair[0] == new_pair[0]:
			new_pair_list.append(new_pair)
			new_pair = None
		else:
			new_pair_list.append(pair)
	if new_pair:
		new_pair_list.append(new_pair)
	return new_pair_list

