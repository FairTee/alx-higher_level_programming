#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes;
	unsigned long int size, i;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;
	size = PyBytes_Size(p);

	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	printf("  first %lu bytes:", size > 10 ? 10 : size);

	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf(" %02x", bytes->ob_sval[i] & 0xFF);
	}

	printf("\n");
}

/**
 * print_python_list - Prints information about a Python list
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list;
	unsigned long int size, i;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetItem(p, i);
		const char *type = element->ob_type->tp_name;

		printf("Element %lu: %s\n", i, type);

		if (PyBytes_Check(element))
		{
			print_python_bytes(element);
		}
	}
}
