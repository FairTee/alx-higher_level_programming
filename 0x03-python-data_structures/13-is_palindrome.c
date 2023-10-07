#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly lnked list is a palindrome
 * @head: Pointer to the first node
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = NULL;
	listint_t *second_half = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	prev_slow->next = NULL;
	reverse_list(&slow, &second_half);

	is_palindrome = compare_lists(*head, second_half);

	reverse_list(&second_half, &slow);
	prev_slow->next = slow;

	return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head
 * @new_head: Pointer to the new head
 */
void reverse_list(listint_t **head, listint_t **new_head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*new_head = prev;
}

/**
 * compare_lists - Compares two linked lists.
 * @list1: Pointer to the first linked list.
 * @list2: Pointer to the second linked list.
 *
 * Return: 1 if the lists are identical, 0 otherwise.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 != NULL && list2 != NULL)
	{
		if (list1->n != list2->n)
			return (0);
		list1 = list1->next;
		list2 = list2->next;
	}

	return (list1 == NULL && list2 == NULL);
}
