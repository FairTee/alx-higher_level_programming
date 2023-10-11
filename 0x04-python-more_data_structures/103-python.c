#include <Python.h>

/**
 * print_python_list - prints information about a Python list
 * @p: a Python object
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		int size = PyList_Size(p);
		int allocated = ((PyListObject *)p)->allocated;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", allocated);

		for (int i = 0; i < size; i++)
		{
			PyObject *element = PyList_GetItem(p, i);
			const char *type = Py_TYPE(element)->tp_name;

			printf("Element %d: %s\n", i, type);
		}
	}
}

/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: a Python object
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
		int size = PyBytes_Size(p);
		const char *string = PyBytes_AsString(p);

		printf("[.] bytes object info\n");
		printf("  size: %d\n", size);
		printf("  trying string: %s\n", string);

		printf("  first %d bytes: ", (size > 10) ? 10 : size);
		for (int i = 0; i < size && i < 10; i++)
		{
			printf("%02x%c", string[i], (i < size - 1) ? ' ' : '\n');
		}
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
