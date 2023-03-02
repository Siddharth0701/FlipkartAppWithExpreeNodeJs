const models = require("../models");
function save(req, res) {
  const product = {
    name: req.body.name,
    price:req.body.price,
    category:req.body.category,
    color:req.body.color,
    description:req.body.description,
    image:req.body.image

  };
  models.Product.create(product)
    .then((result) => {
      res.status(201).json({
        message: "Post create successfully",
        product: result,
      });
    })
    .catch((error) => {
      res.status(500).json({
        message: "Something went wrong",
        error: error,
      });
    });
}

function index(req, res) {
  models.Product.findAll()
    .then((result) => {
      res.status(200).json(result);
    })
    .catch((error) => {
      res.status(500).json({
        message: "something went wrong !",
      });
    });
}
function show(req, res) {
  const id = req.params.id;
  models.Product.findByPk(id)
    .then((result) => {
      if (result) {
        res.status(200).json(result);
      } else {
        res.status(404).json({
          message: "Post not found!",
        });
      }
    })
    .catch((error) => {
      res.status(500).json({
        message: "Something went worong !",
      });
    });
}

function update(req, res) {
  const id = req.params.id;
  const updatedModel = {
    name: req.body.name,
    price:req.body.price,
    category:req.body.category,
    color:req.body.color,
    description:req.body.description,
    image:req.body.image
  };
  models.Product.update(updatedModel, { where: { id: id } })
    .then((result) => {
      res.status(200).json({
        message: "post updated successfully",
        post: updatedModel,
      });
    })
    .catch((error) => {
      res.status(500).json({
        message: "something went wrong !",
        error: error,
      });
    });
}

function deleteProduct(req, res) {
  const id = req.params.id;

  models.Product.destroy({ where: { id: id } })
    .then((result) => {
      res.status(200).json({
        message: "post deleted successfully",
      });
    })
    .catch((error) => {
      res.status(500).json({
        message: "something went wrong !",
        error: error,
      });
    });
}
module.exports = {
  save: save,
  index: index,
  show: show,
  update: update,
  deleteProduct: deleteProduct,
};
