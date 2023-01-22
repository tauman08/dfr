import React from 'react';
import { Link } from 'react-router-dom';

const AuthorItem = ({ author }) => {
    return (
        <tr>
            <td>
                <Link to={`author/${author.first_name}`}>{author.first_name}</Link>
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.birthday_year}
            </td>
        </tr>
    )
}

const AuthorList = ({ authors }) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}

export default AuthorList
