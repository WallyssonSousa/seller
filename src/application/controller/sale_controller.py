from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.application.service.sale_service import SaleService

class SaleController:
    @staticmethod
    @jwt_required()
    def create_sale():
        data = request.get_json() or {}
        seller_id = get_jwt_identity()

        product_id = data.get("product_id")
        quantity = data.get("quantity")

        if not all([product_id, quantity]):
            return make_response(jsonify({"error": "Campos obrigatórios faltando"}), 400)

        sale, err = SaleService.create_sale(seller_id, product_id, quantity)
        if err:
            return make_response(jsonify({"error": err}), 400)

        return make_response(jsonify({
            "message": "Venda realizada com sucesso",
            "sale": sale.to_dict()
        }), 201)

    @staticmethod
    @jwt_required()
    def list_sales():
        sales = SaleService.list_sales()
        return make_response(jsonify({"sales": sales}), 200)

    @staticmethod
    @jwt_required()
    def get_sale(sale_id):
        sale = SaleService.get_sale_by_id(sale_id)
        if not sale:
            return make_response(jsonify({"error": "Venda não encontrada"}), 404)
        return make_response(jsonify({"sale": sale}), 200)
    
    @staticmethod
    @jwt_required()
    def inactivate_sale(sale_id):
        sale, err = SaleService.inactive_sale(sale_id)
        if err:
            return make_response(jsonify({"error": err}), 400)
        
        return make_response(jsonify({
            "message": "Venda inativada com sucesso",
            "sale": sale.to_dict()
        }), 200)
