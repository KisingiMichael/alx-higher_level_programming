#include "lists.h"
#include <stdlib.h>
#include <unistd.h>

/**
 * insert_node - function to insert an element in ordered list
 * @head: pointer to the pointer of the first element of the list
 * @number: node to insert a new node
 *
 * Return: Address of an inserted node or NUL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new_node->next = *head;
		return (*head = new_node);
	}
	else
	{
		while (current_node && current_node->n < number)
		{
			temp = current_node;
			current_node = current_node->next;
		}
		temp->next = new_node;
		new_node->next = current_node;
	}
	return (new_node);
}
