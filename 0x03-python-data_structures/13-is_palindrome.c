#include "lists.h"

listint_t *listint_reverse(listint_t **head);

/**
 * listint_reverse - Function to reverse a singly linked list
 * @head: pointer to the first node of the reversed list
 *
 * Return: return pointer to first head element
 */
listint_t *listint_reverse(listint_t **head)
{
	listint_t *node = *head, *next, *prev_node = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev_node;
		prev_node = node;
		node = next;
	}
	*head = prev_node;
	return (*head);
}

/**
 * is_palindrome - check id the list is palindrome
 * @head: pointer to first element of the list
 *
 * Return: 0, if not palindrome and 1, if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev_node, *mid_node;
	size_t size = 0, x;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}
	for (x = 0; x < (size / 2) - 1; x++)
		tmp = tmp->next;
	if ((size % 2) == 0 && tmp->next != tmp->next->next)
		return (0);

	tmp = tmp->next->next;
	rev_node = listint_reverse(&tmp);
	mid_node = rev_node;

	tmp = *head;
	while (rev_node)
	{
		if (tmp->next != rev_node->next)
			return (0);
		tmp = tmp->next;
		rev_node = rev_node->next;
	}
	listint_reverse(&mid_node);
	return (1);
}
