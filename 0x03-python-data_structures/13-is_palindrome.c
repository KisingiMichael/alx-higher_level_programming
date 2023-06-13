#include "lists.h"

/**
 * is_palindrome - check id the list is palindrome
 * @head: pointer to first element of the list
 *
 * Return: 0, if not palindrome and 1, if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int my_values[9999], x = 0, c = 0;

	if ((!*head) || (!head))
		return (1);
	while (node)
	{
		my_values[x] = node->n;
		node = node->next;
		x++;
	}
	x--;
	while (x >= 0 && c <= x)
	{
		if (my_values[x] != my_values[c])
		{
			return (0);
		}
		x--;
		c++;
	}
	return (1);
}
