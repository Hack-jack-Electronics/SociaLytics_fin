from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
#from langflow import Langflow
from datetime import datetime
import json
import random  # For demo data generation
from flask_cors import CORS
from templates.request import ask_aix



app = Flask(__name__)
CORS(app)
app.secret_key = os.urandom(24)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///langflow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Langflow client
#langflow_client = Langflow(api_url="http://localhost:7860")

# Database Models remain the same...
# Your Flask app.py - add this route for the dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/chart-data', methods=['GET'])
def get_chart_data():
    """Generate real-time chart data"""
    try:
        # In a real application, you would fetch this from your database
        # This is demo data that changes on each request
        post_types = ['Reels', 'Carousels', 'Static Posts']
        engagement_data = [random.uniform(30, 50) for _ in range(3)]
        distribution_data = [random.uniform(20, 45) for _ in range(3)]
        
        return jsonify({
            'success': True,
            'data': {
                'engagement': {
                    'labels': post_types,
                    'datasets': [{
                        'label': 'Engagement by Post Type',
                        'data': engagement_data
                    }]
                },
                'distribution': {
                    'labels': post_types,
                    'datasets': [{
                        'label': 'Content Distribution',
                        'data': distribution_data
                    }]
                }
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/ask-ai', methods=['POST'])
def ask_ai():
    """Process AI questions and return context-aware responses"""
    try:
        question = request.json.get('question')
        
        response = ask_aix(question)
        print(response)
        return jsonify({
            'success': True,
            'response': response
        })
    except Exception as e:
        
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    """Get real-time analytics data"""
    try:
        # Generate demo data that changes each time
        data = {
            'engagement_rate': round(random.uniform(3.5, 5.5), 1),
            'total_interactions': random.randint(10000, 15000),
            'best_performing': random.choice(['Reels', 'Carousels', 'Static Posts'])
        }
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
    


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)