#include "lists.h"

/**
 * check_cycle - check if a list has cycle
 * @list: linked list to be checked
 *
 * Return: 0
 */

int check_cycle(listint_t *list)
{
	listint_t *back = list;
	listint_t *forwd = list;

	if (!list)
		return (0);
	while (back && forwd && forwd->next)
	{
		back = back->next;
		forwd = forwd->next->next;
		if (back == forwd)
			return (1);
	}
	return (0);
}
