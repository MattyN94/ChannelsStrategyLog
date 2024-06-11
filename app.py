from flask import Flask, request, jsonify, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('uploads.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY,
            channel TEXT,
            upload_type_monday TEXT,
            upload_length_monday INTEGER,
            upload_type_tuesday TEXT,
            upload_length_tuesday INTEGER,
            upload_type_wednesday TEXT,
            upload_length_wednesday INTEGER,
            upload_type_thursday TEXT,
            upload_length_thursday INTEGER,
            upload_type_friday TEXT,
            upload_length_friday INTEGER,
            upload_type_saturday TEXT,
            upload_length_saturday INTEGER,
            upload_type_sunday TEXT,
            upload_length_sunday INTEGER
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    conn = sqlite3.connect('uploads.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO uploads (
            channel, 
            upload_type_monday, upload_length_monday, 
            upload_type_tuesday, upload_length_tuesday,
            upload_type_wednesday, upload_length_wednesday,
            upload_type_thursday, upload_length_thursday,
            upload_type_friday, upload_length_friday,
            upload_type_saturday, upload_length_saturday,
            upload_type_sunday, upload_length_sunday
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data.get('channel'),
        data.get('uploadTypeMonday'), data.get('uploadLengthMonday'),
        data.get('uploadTypeTuesday'), data.get('uploadLengthTuesday'),
        data.get('uploadTypeWednesday'), data.get('uploadLengthWednesday'),
        data.get('uploadTypeThursday'), data.get('uploadLengthThursday'),
        data.get('uploadTypeFriday'), data.get('uploadLengthFriday'),
        data.get('uploadTypeSaturday'), data.get('uploadLengthSaturday'),
        data.get('uploadTypeSunday'), data.get('uploadLengthSunday')
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 200

@app.route('/view')
def view():
    conn = sqlite3.connect('uploads.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM uploads')
    rows = cursor.fetchall()
    conn.close()
    return render_template_string('''
        <h1>Stored Upload Data</h1>
        <table border="1">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Channel</th>
                    <th>Upload Type Monday</th>
                    <th>Upload Length Monday</th>
                    <th>Upload Type Tuesday</th>
                    <th>Upload Length Tuesday</th>
                    <th>Upload Type Wednesday</th>
                    <th>Upload Length Wednesday</th>
                    <th>Upload Type Thursday</th>
                    <th>Upload Length Thursday</th>
                    <th>Upload Type Friday</th>
                    <th>Upload Length Friday</th>
                    <th>Upload Type Saturday</th>
                    <th>Upload Length Saturday</th>
                    <th>Upload Type Sunday</th>
                    <th>Upload Length Sunday</th>
                </tr>
            </thead>
            <tbody>
                {% for row in rows %}
                <tr>
                    <td>{{ row[0] }}</td>
                    <td>{{ row[1] }}</td>
                    <td>{{ row[2] }}</td>
                    <td>{{ row[3] }}</td>
                    <td>{{ row[4] }}</td>
                    <td>{{ row[5] }}</td>
                    <td>{{ row[6] }}</td>
                    <td>{{ row[7] }}</td>
                    <td>{{ row[8] }}</td>
                    <td>{{ row[9] }}</td>
                    <td>{{ row[10] }}</td>
                    <td>{{ row[11] }}</td>
                    <td>{{ row[12] }}</td>
                    <td>{{ row[13] }}</td>
                    <td>{{ row[14] }}</td>
                    <td>{{ row[15] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    ''', rows=rows)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
